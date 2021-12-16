# Les bonnes pratiques - Livecode

Pratiquons le **TDD** avec un problème de distributeur automatique.

La machine accepte **4 pièces** :

- **NICKEL** (5 cents)
- **DIME** (10 cents)
- **QUARTER** (25 cents)
- **DOLLAR** (100 cents)

La machine vend ces articles :

- **A** - Biscuits au chocolat - 1$
- **B** - Une canette de coca - 1.20$
- **C** - Une bouteille d'eau - 0.85$

Le distributeur automatique devrait permettre :

- À un agent de service de remplir les articles
- À un utilisateur d'introduire des pièces de monnaie et appuyer sur l'une des touches pour obtenir un article, et récupérer de la monnaie.

## Configuration

```bash
mkdir vending-machine && cd $_
pipenv --python 3.8
pipenv install nose
mkdir tests
touch machine.py
touch tests/test_machine.py

# Nous pouvons maintenant éxecuter :
pipenv run nosetests # => 0 tests for now
```

Bootstrap de la classe de test :

```python
# tests/test_machine.py
import unittest

class MachineTest(unittest.TestCase):
    pass
```

## Solution

Veuillez ne pas regarder _avant_ le livecode !

<details><summary markdown="span">Voir la solution
</summary>

```python
# test/test_machine.py
import unittest
from machine import Machine, Rack, Coin

class MachineTest(unittest.TestCase):
    def test_can_refill_biscuits(self):
        racks = [ Rack("A", "", 100) ]
        machine = Machine(racks)
        machine.refill("A", 3)
        self.assertEqual(machine.racks["A"].quantity, 3)

    def test_user_can_buy_item_a(self):
        racks = [ Rack("A", "", 100) ]
        machine = Machine(racks, 0)
        machine.refill("A", 1)
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("A")
        self.assertTrue(outcome)
        self.assertEqual(machine.racks["A"].quantity, 0)
        self.assertEqual(machine.amount, 0)
        self.assertEqual(machine.coins[Coin.DOLLAR], 1)

    def test_user_get_its_change_back(self):
        racks = [ Rack("C", "", 85) ]
        machine = Machine(racks, 10) # Ten coins each
        machine.refill("C", 1)
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("C")
        self.assertEqual(machine.coins[Coin.DIME], 9)
        self.assertEqual(machine.coins[Coin.NICKEL], 9)
```

```python
# machine.py
from enum import Enum

class Rack:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0

class Coin(Enum):
    NICKEL = 5
    DIME = 10
    QUARTER = 25
    DOLLAR = 100

class Machine:
    def __init__(self, racks, coin_count = 10):
        self.racks = dict((r.code, r) for r in racks)
        self.coins = dict((coin, coin_count) for coin in Coin)
        self.amount = 0

    def refill(self, code, quantity):
        self.racks[code].quantity += quantity

    def insert(self, coin):
        self.coins[coin] += 1
        self.amount += coin.value

    def press(self, code):
        rack = self.racks[code]
        if rack.quantity > 0:
            if self.amount >= rack.price:
                self.racks[code].quantity -= 1
                self.__give_change(self.amount - rack.price)
                self.amount -= rack.price
                return True
            else:
                # TODO: informer l'utilisateur que plus de pièces sont nécessaires !
                return False
        else:
            # TODO: informer l'utilisateur que ce produit est épuisé !
            return False

    def __give_change(self, change):
        if change == 0:
            return
        else:
            for coin in reversed(Coin):
                count = change // coin.value
                change = change % coin.value
                self.coins[coin] -= count
```

</details>
