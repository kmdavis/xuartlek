---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Wihsaak"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Wihsaak"
level: 6
source: "Monster Core 2"
aon_id: "creature-4535"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4535"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Wihsaak"
level: "Creature 6"
size: "Medium"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 14
perception:
  - name: "Perception"
    desc: "Perception +14; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Chthonian|Chthonian]], [[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]], Requian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +13, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +15, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15"
abilityMods: [4, 5, 4, 1, 2, 3]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the [[srd/pf2e/compendium/spells/rituals/binding-circle|_binding circle_]] ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +14; __Ref__: +15; __Will__: +14"
hp: 105
health:
  - name: "HP"
    desc: "105; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fear|fear]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
abilities_mid:
  - name: "Swarmwalker"
    desc: "Swarms of animals and other unintelligent creatures instinctively leave a wihsaak alone. A wihsaak is immune to the damage from and effects of swarms with an Intelligence of –5."
speed: "30 feet, fly 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +17 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|unholy]]) __Damage__ 2d10+7 slashing plus 1d4 spirit"
abilities_bot:
  - name: "Droning Distraction"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]])"
  - name: "Effect"
    desc: "The wihsaak beats its wings rapidly, creating a buzzing drone that numbs creatures' minds. Each creature within 100 feet must attempt a DC 23 Will save. They are then temporarily immune for 1 minute."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]] and [[srd/pf2e/compendium/rules-elements/conditions#Stupefied|stupefied]] 1 for 1 round."
  - name: "Critical Failure"
    desc: "The creature is confused for 1 round and stupefied 2 for 1 minute."
  - name: "Skip Between"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/teleportation|teleportation]]) The sahkil moves from [[srd/pf2e/compendium/gm/planes#The Universe|the Universe]] to the [[srd/pf2e/compendium/gm/planes#Ethereal Plane|Ethereal Plane]] or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23 - __Cantrips (3rd)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/blur|Blur]], [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]] - __3rd__ [[srd/pf2e/compendium/spells/rank-1/fear|Fear]], [[srd/pf2e/compendium/spells/rank-2/vomit-swarm|Vomit Swarm]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/suggestion|Suggestion]]"
sourcebook: "_Monster Core 2_, page 275."
```

```encounter-table
name: Wihsaak
creatures:
  - 1: Wihsaak
```
