---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gnokesh"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/archon
  - pf2e/creature/trait/celestial
  - pf2e/creature/trait/holy
  - pf2e/creature/trait/medium
statblock: inline
name: "Gnokesh"
level: 5
source: "Monster Core 2"
aon_id: "creature-4064"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4064"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Gnokesh"
level: "Creature 5"
size: "Medium"
trait_01: "Archon"
trait_02: "Celestial"
trait_03: "Holy"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Chthonian, Diabolic, Draconic, Empyrean, Fey, Sakvroth, Shadowtongue, Utopian; _truespeech_"
skills:
  - name: "Skills"
    desc: "Arcana +12, Diplomacy +11, Lore +16, Nature +11, Occultism +12, Religion +13, Society +12"
abilityMods: [2, 4, 0, 5, 4, 4]
abilities_top:
  - name: "Light of Diligence"
    desc: "(divine) The gnokesh has devoted themselves to the thorough study of one particular Lore skill (with the bonus found in the Skills section above), such as Heaven Lore or Warfare Lore. If the gnokesh rolls a critical failure to Recall Knowledge with this skill, they get a failure instead. They can also use the Aid action for this skill without first preparing to help, and they automatically grant a +3 circumstance bonus."
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +9; __Ref__: +12; __Will__: +15 +1 status to all saves vs. magic"
hp: 70
health:
  - name: "HP"
    desc: "70; __Immunities__ fear; __Weaknesses__ unholy 5"
abilities_mid:
  - name: "Archon's Protection"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy damages the archon's ally and both are within 15 feet of the archon"
  - name: "Effect"
    desc: "The ally gains resistance 5 to all damage against the triggering damage, and the archon can make a Strike against the enemy."
  - name: "Light of Diligence"
    desc: "⬲ (divine, fortune)"
  - name: "Trigger"
    desc: "A willing ally within 15 feet critically fails at a check"
  - name: "Effect"
    desc: "The ally gets a failure instead and becomes immune to Light of Diligence for 1 minute."
speed: "25 feet, fly 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tome +13 (Divine, Finesse, Holy) __Damage__ 1d6+6 bludgeoning plus 1d6 spirit"
  - name: "Ranged"
    desc: "⬻ light ray +13 (Divine, Fire, Holy, Light, Magical, range increment 20 feet, Spirit) __Damage__ 2d6 fire plus 2d6 spirit"
abilities_bot:
  - name: "Spells"
    desc: "DC 22, attack +14 - __Cantrips (5th)__ Light, Message, Telekinetic Hand - __1st__ Sure Strike (×3) - __2nd__ Silence - __3rd__ Calm, Clairaudience - __4th__ Clairvoyance, Translocate (at will) - __Constant (5th)__ Truespeech"
  - name: "Alluring Knowledge"
    desc: "⬺ (Divine, Holy, Light, Mental)"
  - name: "Frequency"
    desc: "once per hour"
  - name: "Effect"
    desc: "A twisting scroll of runes made of light appears in an unoccupied square within 60 feet. Each creature adjacent to the runes must succeed at a DC 22 basic Will save or take 3d8 mental damage and be fascinated with the magical text as long as it remains. The magical text lasts until the end of the gnokesh's next turn."
sourcebook: "_Monster Core 2_, page 36."
```

```encounter-table
name: Gnokesh
creatures:
  - 1: Gnokesh
```
