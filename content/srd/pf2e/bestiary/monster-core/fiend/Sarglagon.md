---
noteType: pf2eMonster
aliases: "Sarglagon"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/devil
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/large
statblock: inline
name: "Sarglagon"
level: 8
source: "Monster Core"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2908"
socialImage: og-image.png
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Sarglagon"
level: "Creature 8"
size: "Large"
trait_01: "Amphibious"
trait_02: "Devil"
trait_03: "Fiend"
trait_04: "Unholy"
modifier: 18
perception:
  - name: "Perception"
    desc: "+18; greater darkvision, see the unseen"
languages: "[[srd/pf2e/compendium/rules-elements/Languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/Languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Arcana|Arcana]] +14, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/Deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/Diplomacy|Diplomacy]] +15, [[srd/pf2e/compendium/rules-elements/skills/Intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/Stealth|Stealth]] +15"
abilityMods: [6, 3, 4, 2, 4, 3]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +13; __Will__: +16 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magic]]"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Fire|fire]]; __Resistances__ physical 5 (except silver), [[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|poison]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Holy|holy]] 5"
abilities_mid:
  - name: "Heavy Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|incapacitation]]) 10 feet. A creature that enters the heavy aura must attempt a DC 23 Will save. It is then temporarily immune for 10 minutes."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/Conditions#Encumbered|encumbered]] while it remains in the area. If the creature is already encumbered, it is [[srd/pf2e/compendium/rules-elements/Conditions#Immobilized|immobilized]] while it remains within the aura."
  - name: "Critical Failure"
    desc: "As failure, but the effect persists for 3 rounds after leaving the aura."
  - name: "Stygian Guardian"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature or object within the sarglagon's reach is targeted by an attack"
  - name: "Effect"
    desc: "The sarglagon interposes themself, giving the creature or object standard cover against the attack (+2 circumstance bonus to AC), or greater cover (+4 circumstance bonus to AC) if the sarglagon was already granting it lesser cover."
speed: "25 feet, fly 25 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d12+9 piercing"
  - name: "Melee"
    desc: "⬻ tentacle arm +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Unholy|Unholy]]) __Damage__ 2d8+9 bludgeoning plus sarglagon venom"
abilities_bot:
  - name: "Drown"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Water|Water]]) The sarglagon conjures murky water to fill the lungs of a creature within 30 feet of it that can't breathe water. The target must attempt a DC 26 Fortitude save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target coughs up water and is [[srd/pf2e/compendium/rules-elements/Conditions#Sickened|sickened 1]]."
  - name: "Failure"
    desc: "The target is holding its breath. The only action it can take is to attempt a Fortitude save against Drown to expel the water, which is a single action."
  - name: "Critical Failure"
    desc: "The target falls [[srd/pf2e/compendium/rules-elements/Conditions#Unconscious|unconscious]] and begins suffocating. If the target succeeds at its Fortitude save while suffocating, it coughs up the water and can breathe again."
  - name: "Sarglagon Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage and [[srd/pf2e/compendium/rules-elements/Conditions#Clumsy|clumsy 1]] (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and clumsy 2 (1 round)"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +18 - __4th__ [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-4/Hydraulic Torrent|Hydraulic Torrent]], [[srd/pf2e/compendium/spells/rank-4/Unfettered Movement|Unfettered Movement]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/Control Water|Control Water]], [[srd/pf2e/compendium/spells/rank-4/Translocate|Translocate]] - __Constant (2nd)__ [[srd/pf2e/compendium/spells/rank-2/See the Unseen|See the Unseen]]"
  - name: "Rituals"
    desc: "DC 23 - __1st__ [[srd/pf2e/compendium/spells/rituals/Diabolic Pact|Diabolic Pact]]"
sourcebook: "_Monster Core_, page 89."
```

```encounter-table
name: Sarglagon
creatures:
  - 1: Sarglagon
```
