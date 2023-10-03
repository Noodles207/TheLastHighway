import random



"""
EFFECTS AND WHAT THEY DO
---- healing ----
healWithoutOverheal - heals the player by the "power" value, up to max health.
healWithOverheal - flatly adds the amount to be healed to the player's max health, initiating overheal.
healPercent - heals the player by the percentage specified by the power value.
healOverhealPercent - heals the player by the percentage specified by the power value. Can overheal.
-NOTE: since you can stack effects in an item's description, if you wanted to, say, heal to max then overheal, put the max heal first.-
---- buffs, debuffs ----
empty... for now
"""

"""
ITEM DECLARATIONS
-note: an "item" is a consumable, bit, or bob that doesn't do damage directly.
ITEM NAMING SCHEME:
systemNane = ["itemName", maxUses,"effect1", power, "effect2", power..., "STOP"]
EFFECTS WILL BE READ FROM LEFT TO RIGHT, AND APPLIED AS READ!
I'll add more stuff as needed
"""

healthPotion = ["Health Potion", 3, "healWithoutOverheal", 20]

"""
ENEMIES & MODIFIERS
ENEMY NAMING SCHEME:
enemyType = [enemyName, maxHealth, health, attackOne, attackTwo, attackThree, maxXP, minXP, modifier, modifier...]
"""
