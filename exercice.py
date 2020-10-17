#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from structs import Queue, Stack


def reverse_data(data: list = None):
    # TODO: Demander 10 valeurs à l'utilisateur,
    # les stocker dans une structure de données,
    # et les retourner en ordre inverse, sans utiliser de liste.

    if data is None:
       pass
            
    reversed_data = None  # Stocker le résultat ici

    return reversed_data


def delete_nth_from_stack(data: Stack, position: int) -> Stack:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    return Stack()


def delete_nth_from_queue(data: Queue, position: int) -> Queue:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    return Queue()


def sort_stack(data: Stack) -> Stack:
    # TODO: Retourner la séquence triée
    
    ma_liste = [1,6,5,8]
     lifo = LifoQueue()
        for element in ma_liste:
            lifo.put(element)
            
        #liste = [lifo.pop() for _ in range(lifo.qsize())], qsize pas fiable si plusieurs personnes en même temps, mais si tout seul très bien, prend la longueur au début, si quelqu'un ajoute un élément entre temps je ne viderais pas complètement la pile
        liste = []
        while not lifo.empty():
            liste.append(lifo.get())
            
        liste_trie = sorted(liste)
        for element in liste_trie:
            lifo.put(element)
            
   """ ajout d'un nouvel élément dans notre pile triée
    avec une liste
    variable = 5
    
    liste_tmp = []
    while not lifo.empty():
            current = lifo.get()
            if current <= variable:
                lifo.put(current)
                lifo.put(variable)
                break
            else:
                liste_tmp.append(lifo.get())
    for element in reversed(liste_tmp):
        lifo.put(element)
        
     while not lifo.empty(): pour afficher
        print(lifo.get())
        
    avec une autre pile
    variable = 5
    
    autre_pile = LifoQueue()
    while not lifo.empty():
            current = lifo.get()
            if current <= variable:
                lifo.put(current)
                lifo.put(variable)
                break
            else:
                autre_pile.put(lifo.get())
                
    while not autre_pile.empty():
        lifo.put(autre_pile.get())
        
     while not lifo.empty(): pour afficher
        print(lifo.get())"""
    return Stack()


def sort_queue(data: Queue) -> Queue:
    # TODO: Retourner la séquence triée
    return Queue()


def string_and_structs(string: str) -> tuple:
    # TODO: Parcourez la chaîne de caractères.
    # Si le caractère est une lettre, on l'ajoute dans fifo.
    # Sinon, on retire un élément de fifo pour l'insérer dans lifo.

    fifo, lifo = Queue(), Stack()

    return fifo, lifo


def main() -> None:
    print("On inverse des données...")
    print(f"Résultat: {reverse_data()}")

    n = 4
    lifo = Stack()
    lifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la pile et on obtient: {delete_nth_from_stack(lifo, n)}")

    n = 6
    fifo = Queue()
    fifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la file et on obtient: {delete_nth_from_queue(fifo, n)}")

    lifo = Stack()
    lifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_queue(lifo)}")

    fifo = Queue()
    fifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_queue(fifo)}")

    sequence = "te!eYy.E6e/T"
    print(f"Le résulat de la manipulation de la séquence: {string_and_structs(sequence)}")


if __name__ == '__main__':
    main()
