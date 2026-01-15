from retriever import retrieve_for_and_against
from lawyer import argue
def run_benchmark(name, db_dir, claims):
    print(f"\n===== Benchmark: {name} =====\n")

    for c in claims:
        docs_for, docs_against = retrieve_for_and_against(
            c,
            db_dir=db_dir
        )
        answer = argue(c, docs_for, docs_against)

        print("CLAIM:", c)
        print(answer)
        print("-" * 80)


claim = input("Enter your claim: ")

docs_for, docs_against = retrieve_for_and_against(claim)
response = argue(claim, docs_for, docs_against)

print("\n--- RAG Lawyer Response ---\n")
print(response)
run_benchmark("Sample Benchmark", "db", [ claim 
    ,])


