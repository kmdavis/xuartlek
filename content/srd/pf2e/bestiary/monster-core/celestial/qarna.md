---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Qarna"
tags:
  - pf2e/creature/level/4
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Qarna"
level: 4
source: "Monster Core"
aon_id: "creature-2833"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2833"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Qarna"
level: "Creature 4"
size: "Medium"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 11
perception:
  - name: "Perception"
    desc: "Perception +11; darkvision"
languages: "Diabolic, Draconic, Empyrean, Utopian; _truespeech_"
skills:
  - name: "Skills"
    desc: "Acrobatics +12, Intimidation +11, Nature +11, Religion +9, Stealth +10, Survival +11, Athletics +11"
abilityMods: [3, 4, 3, 1, 3, 1]
abilities_top:
  - name: "Items"
    desc: "Composite Longbow (20 arrows)"
ac: 22
armorclass:
  - name: "AC"
    desc: "22; __Fort__: +11; __Ref__: +10; __Will__: +11 +1 status to all saves vs. magic"
hp: 65
health:
  - name: "HP"
    desc: "65; __Immunities__ fear; __Weaknesses__ unholy 5"
abilities_mid:
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 5 to all damage against the triggering damage and the archon can make a Strike against the enemy."
speed: "35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ horn +13 (Holy, Magical) __Damage__ 1d8+9 piercing plus Push"
  - name: "Ranged"
    desc: "⬻ composite longbow +14 (Holy, deadly d10, Magical, Propulsive, range increment 100 feet, volley 30 feet) __Damage__ 1d8+7 piercing"
abilities_bot:
  - name: "Archon's Pursuit"
    desc: "⬺"
  - name: "Frequency"
    desc: "once per day"
  - name: "Requirements"
    desc: "The qarna saw another creature teleport within the last round and has at least one _translocate_ spell remaining"
  - name: "Effect"
    desc: "The qarna casts one of their _translocate_ spells, which is heightened to 5th rank and causes the qarna to arrive in an unoccupied space it chooses within 30 feet of the creature it's pursuing. If the creature is too far away, the qarna arrives as close as possible."
  - name: "Distracting Arrow"
    desc: "⬺ (Divine, Mental) The qarna makes a composite longbow Strike. If it hits, the arrow lodges in the target and that creature's senses focus on the archon, leaving all else blurry. That creature takes a –2 status penalty to attack rolls and Perception checks against any target other than the qarna. The creature can Interact to remove the arrow, which ends the effect."
  - name: "Touch of Charity"
    desc: "⬻ (Divine, Healing, Manipulate, Vitality) The qarna touches a willing living creature to take on that creature's wounds. The qarna transfers up to 30 of their own HP to the touched creature. (The qarna can't transfer more HP than they currently have.)"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 21 - __Cantrips (2nd)__ Light - __1st__ Charm (animals only; ×3), Sure Strike (×3) - __2nd__ Animal Messenger (×3) - __4th__ Translocate (×3) - __Constant (5th)__ Truespeech"
sourcebook: "_Monster Core_, page 27."
```

```encounter-table
name: Qarna
creatures:
  - 1: Qarna
```
