---
obsidianUIMode: preview
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
aon_id: "creature-2908"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2908"
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
    desc: "Perception +18; greater darkvision, see the unseen"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Diabolic|Diabolic]], [[srd/pf2e/compendium/rules-elements/languages#Empyrean|Empyrean]]; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +14, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +18, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +15, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +15, [[srd/pf2e/compendium/rules-elements/skills/intimidation|Intimidation]] +17, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +15"
abilityMods: [6, 3, 4, 2, 4, 3]
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +18; __Ref__: +13; __Will__: +16 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magic]]"
hp: 120
health:
  - name: "HP"
    desc: "120; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]; __Resistances__ physical 5 (except silver), [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]] 10; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/holy|holy]] 5"
abilities_mid:
  - name: "Heavy Aura"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]]) 10 feet. A creature that enters the heavy aura must attempt a DC 23 Will save. It is then temporarily immune for 10 minutes."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature is [[srd/pf2e/compendium/rules-elements/conditions#Encumbered|encumbered]] while it remains in the area. If the creature is already encumbered, it is [[srd/pf2e/compendium/rules-elements/conditions#Immobilized|immobilized]] while it remains within the aura."
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
    desc: "⬻ fangs +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d12+9 piercing"
  - name: "Melee"
    desc: "⬻ tentacle arm +20 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/unholy|Unholy]]) __Damage__ 2d8+9 bludgeoning plus sarglagon venom"
abilities_bot:
  - name: "Drown"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|Incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/water|Water]]) The sarglagon conjures murky water to fill the lungs of a creature within 30 feet of it that can't breathe water. The target must attempt a DC 26 Fortitude save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target coughs up water and is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]]."
  - name: "Failure"
    desc: "The target is holding its breath. The only action it can take is to attempt a Fortitude save against Drown to expel the water, which is a single action."
  - name: "Critical Failure"
    desc: "The target falls [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]] and begins suffocating. If the target succeeds at its Fortitude save while suffocating, it coughs up the water and can breathe again."
  - name: "Sarglagon Venom"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/poison|Poison]])"
  - name: "Saving Throw"
    desc: "DC 26 Fortitude"
  - name: "Maximum Duration"
    desc: "6 rounds"
  - name: "Stage 1"
    desc: "2d6 poison damage and [[srd/pf2e/compendium/rules-elements/conditions#Clumsy|clumsy 1]] (1 round)"
  - name: "Stage 2"
    desc: "3d6 poison damage and clumsy 2 (1 round)"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +18 - __4th__ [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will), [[srd/pf2e/compendium/spells/rank-4/hydraulic-torrent|Hydraulic Torrent]], [[srd/pf2e/compendium/spells/rank-4/unfettered-movement|Unfettered Movement]] - __5th__ [[srd/pf2e/compendium/spells/rank-5/control-water|Control Water]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __Constant (2nd)__ [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]]"
  - name: "Rituals"
    desc: "DC 23 - __1st__ [[srd/pf2e/compendium/spells/rituals/diabolic-pact|Diabolic Pact]]"
sourcebook: "_Monster Core_, page 89."
```

```encounter-table
name: Sarglagon
creatures:
  - 1: Sarglagon
```
