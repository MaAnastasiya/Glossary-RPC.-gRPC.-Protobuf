import grpc
from proto import glossary_pb2, glossary_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = glossary_pb2_grpc.GlossaryServiceStub(channel)

    # Добавление нескольких терминов
    print("Adding terms:")
    terms_to_add = [
        glossary_pb2.Term(keyword="Python", description="A programming language."),
        glossary_pb2.Term(keyword="gRPC", description="A high-performance RPC framework."),
        glossary_pb2.Term(keyword="Protobuf", description="A method for serializing structured data.")
    ]

    for term in terms_to_add:
        response = stub.AddTerm(term)
        print(f"Added: {term.keyword} - {response.message}")

    # Получение всех терминов
    print("\nFetching all terms:")
    all_terms = stub.GetAllTerms(glossary_pb2.Empty())
    for term in all_terms.terms:
        print(f"{term.keyword}: {term.description}")

    # Удаление термина
    print("\nDeleting a term:")
    response = stub.DeleteTerm(glossary_pb2.Keyword(keyword="gRPC"))
    print(f"Deleted: {response.message}")

    # Получение всех терминов после удаления
    print("\nFetching all terms after deletion:")
    all_terms = stub.GetAllTerms(glossary_pb2.Empty())
    for term in all_terms.terms:
        print(f"{term.keyword}: {term.description}")

    # Обновление термина
    print("\nUpdating a term:")
    updated_term = glossary_pb2.Term(keyword="Python", description="A powerful programming language.")
    response = stub.UpdateTerm(updated_term)
    print(f"Updated: {updated_term.keyword} - {response.message}")

    # Получение всех терминов после обновления
    print("\nFetching all terms after update:")
    all_terms = stub.GetAllTerms(glossary_pb2.Empty())
    for term in all_terms.terms:
        print(f"{term.keyword}: {term.description}")


if __name__ == '__main__':
    run()