---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Coven Aspirant"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Coven Aspirant"
level: 2
source: "NPC Core"
aon_id: "creature-3535"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3535"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "NPC"
name: "Coven Aspirant"
level: "Creature 2"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7"
languages: "Common, Fey, Jotun"
skills:
  - name: "Skills"
    desc: "Deception +7, Intimidation +5, Medicine +5, Occultism +8, Stealth +7, Survival +5"
abilityMods: [2, 1, 1, 4, 1, 1]
abilities_top:
  - name: "Items"
    desc: "cauldron, Dagger, Dart (4)"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +7; __Ref__: +7; __Will__: +9 (shared confidence)"
hp: 35
health:
  - name: "HP"
    desc: "35"
abilities_mid:
  - name: "Shared Confidence"
    desc: "When a coven aspirant is within 30 feet of at least two allies, they and their allies gain a +1 status bonus to Will saves."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +8 (Agile, versatile S) __Damage__ 1d4+4 slashing"
  - name: "Melee"
    desc: "⬻ fist +8 (Agile, Nonlethal, Unarmed) __Damage__ 1d4+4 bludgeoning"
  - name: "Ranged"
    desc: "⬻ dart +7 (Agile, thrown 20 feet) __Damage__ 1d4+4 piercing"
abilities_bot:
  - name: "Forge Pact"
    desc: "⬻ (Auditory, Concentrate, Linguistic, Mental, Occult) The coven aspirant forms a temporary coven with two or more willing creatures within 30 feet, all of whom must be able to cast spells. Members of the temporary coven can cast _charm_, _entangling flora_, and _illusory disguise_ as 2nd-rank occult innate spells at will, using DC 17 or their spellcasting DC, whichever is higher. The coven is dissolved after 3 rounds or when all but one member is dead, whichever comes first. A creature can be a member of only one temporary coven at a time and can join a temporary coven no more than once per 24 hours. Unusual Covens Though rare, covens can form that include non-hags, as long as at least two hags are a part of the coven. Changeling, vengeful nature spirits, intelligent undead, and fiends sometimes ally themselves with hags. The unusual composition of the coven alters the spells granted by the partnership, typically replacing the _cursed metamorphosis_ spell with a spell appropriate to the coven's new member."
spellcasting:
  - name: "Occult Prepared Spells"
    desc: "DC 18, attack +10 - __Cantrips (1st)__ Daze, Figment, Light, Prestidigitation, Void Warp - __1st__ Fear, Grim Tendrils, Ill Omen __Witch Hex Spells 1 Focus Point,__ DC 18 - __Cantrips (1st)__ Shroud of Night - __1st__ Needle of Vengeance"
sourcebook: "_NPC Core_, page 97."
```

```encounter-table
name: Coven Aspirant
creatures:
  - 1: Coven Aspirant
```
