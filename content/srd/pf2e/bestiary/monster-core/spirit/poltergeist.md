---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Poltergeist"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/incorporeal
  - pf2e/creature/trait/spirit
  - pf2e/creature/trait/undead
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Poltergeist"
level: 5
source: "Monster Core"
aon_id: "creature-3142"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3142"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Poltergeist"
level: "Creature 5"
size: "Medium"
trait_01: "Incorporeal"
trait_02: "Spirit"
trait_03: "Undead"
trait_04: "Unholy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Common"
skills:
  - name: "Skills"
    desc: "Acrobatics +14, Intimidation +15, Stealth +14"
abilityMods: [-5, 5, 0, -1, 2, 4]
abilities_top:
  - name: "Site Bound"
    desc: "A poltergeist is tied to a location and can't travel more than 120 feet from the place where it was created or formed. Some poltergeists are instead bound to a specific room, building, or similar area."
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +9; __Ref__: +14; __Will__: +13"
hp: 55
health:
  - name: "HP"
    desc: "55 (void healing, rejuvenation); __Immunities__ bleed, death effects, disease, paralyzed, poison, precision, unconscious; __Resistances__ all damage 5 (except force, _ghost touch_, spirit, or vitality; double resistance vs. non-magical)"
abilities_mid:
  - name: "Natural Invisibility"
    desc: "A poltergeist is naturally invisible. It becomes visible only when it uses Frighten."
  - name: "Rejuvenation"
    desc: "(occult) When a poltergeist is destroyed, it reforms, fully healed, where it was destroyed after 2d4 days. A poltergeist can be permanently destroyed only if someone determines the reason for its existence and sets right whatever prevents the spirit from resting."
  - name: "Telekinetic Defense"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature approaches within 10 feet of the poltergeist"
  - name: "Effect"
    desc: "The poltergeist makes a telekinetic object Strike against the triggering creature."
speed: "fly 20 feet"
attacks:
  - name: "Ranged"
    desc: "⬻ telekinetic object +13 (Magical, Occult, range increment 60 feet) __Damage__ 2d12 bludgeoning, piercing, or slashing (depending on object)"
abilities_bot:
  - name: "Frighten"
    desc: "⬻ (Concentrate, Emotion, Fear, Incapacitation, Mental)"
  - name: "Requirements"
    desc: "The poltergeist must be invisible"
  - name: "Effect"
    desc: "The poltergeist becomes visible, appearing as a skeletal, ghostlike humanoid. Each creature within 30 feet must attempt a DC 21 Will save, becoming frightened 2 on a failure. On a critical failure, it's also fleeing for as long as it's frightened. On a success, the creature is temporarily immune for 1 minute. At the start of its next turn, the poltergeist becomes invisible again."
  - name: "Telekinetic Storm"
    desc: "⬺ (Concentrate, Occult) The poltergeist telekinetically throws numerous small objects, such as dozens of pieces of silverware or books, either spreading them out among multiple foes or directing them at one target. When this effect is spread out among multiple foes, the poltergeist makes a telekinetic object Strike at a –2 penalty against each creature within 30 feet. These count as one attack for the poltergeist's multiple attack penalty, and the penalty doesn't increase until after all the attacks.When this effect has only one target, the poltergeist makes a telekinetic object Strike against the target, and the damage increases to 3d12. It deals 1d12 damage on a failure, and no damage on a critical failure. Disturbed Rest One of the most common ways for a poltergeist to form is when its burial site is desecrated by the construction of a dwelling. This is usually an accident, but some creatures intentionally create poltergeists to serve as guardians. Poltergeist Treasure A poltergeist needs items to hurl as weapons, and over the centuries of use, only durable objects survive its rampages. Silver dinnerware, hatchets, and books might all be found in a poltergeist's collection."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 23, attack +13 - __Cantrips (3rd)__ Telekinetic Hand - __3rd__ Telekinetic Maneuver (at will)"
sourcebook: "_Monster Core_, page 268."
```

```encounter-table
name: Poltergeist
creatures:
  - 1: Poltergeist
```
