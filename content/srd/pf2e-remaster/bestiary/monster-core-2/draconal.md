---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Draconal"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/agathion
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/large
statblock: inline
name: "Draconal"
level: 20
source: "Monster Core 2"
aon_id: "creature-4021"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4021"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Draconal"
level: "Creature 20"
size: "Large"
trait_01: "Agathion"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 36
perception:
  - name: "Perception"
    desc: "Perception +36; darkvision"
languages: "Diabolic, Draconic, Empyrean; _speak with animals_, _truespeech_"
skills:
  - name: "Skills"
    desc: "Arcana +38, Crafting +30, Deception +35, Diplomacy +37, Intimidation +35, Medicine +34, Nature +34, Nirvana Lore +36, Religion +36, Society +32, Survival +32"
abilityMods: [10, 5, 8, 8, 10, 9]
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +34; __Ref__: +31; __Will__: +38"
hp: 370
health:
  - name: "HP"
    desc: "370 , regeneration 20 (deactivated by unholy); __Resistances__ spirit 15; __Weaknesses__ unholy 20"
abilities_mid:
  - name: "Dragon's Salvation"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature within the draconal's reach would take damage"
  - name: "Effect"
    desc: "Before applying the damage, the draconal casts _lay on hands_ on the triggering creature."
speed: "30 feet, fly 90 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 (Holy, Magical, reach 15 feet) __Damage__ 3d12+18 piercing plus 4d6 spirit"
  - name: "Melee"
    desc: "⬻ claw +38 (Agile, Holy, Magical, reach 10 feet) __Damage__ 3d8+18 slashing plus 4d6 spirit"
abilities_bot:
  - name: "Champion Focus Spell"
    desc: "DC 46, 3 Focus Points - __10th__ Lay on Hands"
  - name: "Breath of Wisdom"
    desc: "⬺ (Divine, Holy) The draconal breathes a blast of energy that deals 21d6 spirit damage to creatures they choose to damage in a 60-foot cone (DC 44 basic Reflex save). They can make this effect nonlethal for selected creatures in the area or choose not to damage certain creatures at all. They can't use Breath of Wisdom again for 1d4 rounds."
  - name: "Dragon's Wisdom"
    desc: "Draconals embody the core value of wisdom, and all wisdom is obtained through understanding. If a draconal successfully Recalls Knowledge about a creature, they learn their highest weakness in addition to any other obtained knowledge, and any spirit damage they do to that creature becomes damage of their highest known weakness instead. Draconals And Dragons Draconals hold a great respect for dragons, particularly great dragons, but as they rarely visit the mortal Universe, interactions between the two groups tends to be minimal. Despite a general respect for dragonkind, draconals often revile malicious dragons. In times of strife, draconals use their might and wisdom against the forces of wickedness. They stand alongside empyreal and other celestial dragons to face off against unholy forces."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 46, attack +38 - __9th__ Breath of Life, Dispel Magic, Divine Decree, Earthquake, Heal (×3), Implosion, Wrathful Storm - __10th__ Manifestation - __Constant (7th)__ Speak with Animals, Truesight, Truespeech"
sourcebook: "_Monster Core 2_, page 18."
```

```encounter-table
name: Draconal
creatures:
  - 1: Draconal
```
