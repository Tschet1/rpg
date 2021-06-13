#!/usr/bin/env python3

from objects.person import Person, Gender
from graphviz import Graph
from pathlib import Path

def create_whole_family_tree(person: Person, filename: Path):
    head = person
    while(head.father):
        head = head.father
    create_family_tree_with_head(head, filename)


def create_family_tree_with_head(person: Person, filename: Path):
    def iterate_add_person(person: Person, graph, index: int):
        graph.node(f"P{index}", f"{person.name}")
        person_index = index

        if person.spouse:
            index += 1
            graph.node(f"P{index}", f"{person.spouse.name}")
            graph.edge(f"P{index}", f"P{person_index}")

        if person.gender == Gender.MALE and len(person.children) > 0:
            for child in person.children:
                index += 1
                index_end = iterate_add_person(child, graph, index)
                graph.edge(f"P{index}", f"P{person_index}")
                index = index_end

        return index

    g = Graph(format='svg')
    iterate_add_person(person, g, 0)
    g.render(filename, view=False)
