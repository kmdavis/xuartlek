---
noteType: pf2eMonster
aliases: "Gnome Bard"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/gnome
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/small
statblock: inline
name: "Gnome Bard"
level: 1
source: "Monster Core"
aon_url: "https://2e.aonprd.com/NPCs.aspx?ID=3020"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gnome Bard"
level: "Creature 1"
size: "Small"
trait_01: "Gnome"
trait_02: "Humanoid"
modifier: 7
perception:
  - name: "Perception"
    desc: "+7; low-light vision"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/Languages#Fey|Fey]], [[srd/pf2e/compendium/rules-elements/Languages#Gnomish|Gnomish]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +7, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +5, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +7, [[srd/pf2e/compendium/rules-elements/skills/Performance|Performance]] +7, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +5"
abilityMods: [1, 3, 1, 1, 2, 4]
abilities_top:
  - name: "Items"
    desc: "Dagger, Musical Instrument (handheld), Sling (20 bullets)"
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +5; __Ref__: +7; __Will__: +9"
hp: 16
health:
  - name: "HP"
    desc: "16"
abilities_mid:
  - name: "Gnomish Shift"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Primal|primal]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Teleportation|teleportation]])"
  - name: "Trigger"
    desc: "The gnome bard would take damage"
  - name: "Effect"
    desc: "The gnome bard gains resistance 2 to the triggering damage and teleports to an adjacent space."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Versatile|versatile S]]) __Damage__ 1d4+2 piercing"
  - name: "Ranged"
    desc: "⬻ sling +8 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Propulsive|Propulsive]], range increment 50 feet, reload 1) __Damage__ 1d6+1 bludgeoning"
abilities_bot:
  - name: "Do a Jig"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Auditory|Auditory]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Occult|Occult]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|Mental]]) the gnome bard plays a ditty that inspires dance. One creature within 30 feet must make a Will saving throw DC 19."
  - name: "Success"
    desc: "the target is unaffected."
  - name: "Failure"
    desc: "The target must waste 1 action on its next turn dancing."
  - name: "Critical Failure"
    desc: "The target must waste 2 actions on its next turn dancing."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 19, attack +11 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/Courageous Anthem|Courageous Anthem]], [[srd/pf2e/compendium/spells/cantrips/Daze|Daze]], [[srd/pf2e/compendium/spells/cantrips/Figment|Figment]], [[srd/pf2e/compendium/spells/cantrips/Message|Message]], [[srd/pf2e/compendium/spells/cantrips/Prestidigitation|Prestidigitation]], [[srd/pf2e/compendium/spells/cantrips/Summon Instrument|Summon Instrument]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/Charm|Charm]], [[srd/pf2e/compendium/spells/rank-1/Command|Command]] (4 slots)"
sourcebook: "_Monster Core_, page 172."
```

```encounter-table
name: Gnome Bard
creatures:
  - 1: Gnome Bard
```
