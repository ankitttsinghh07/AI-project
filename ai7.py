def forward_chaining(facts, rules):

    new_fact_added = True

    while new_fact_added:
        new_fact_added = False

        for condition, conclusion in rules:

            if all(fact in facts for fact in condition):

                if conclusion not in facts:
                    facts.add(conclusion)
                    print("New fact derived:", conclusion)
                    new_fact_added = True

    return facts


# Initial facts
facts = {"A", "B"}

# Rules (Conditions, Conclusion)
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]

# Apply Forward Chaining
result = forward_chaining(facts, rules)

print("\nFinal Facts:", result)