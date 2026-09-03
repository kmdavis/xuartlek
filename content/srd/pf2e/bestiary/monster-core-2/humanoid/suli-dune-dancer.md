---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Suli Dune Dancer"
tags:
  - pf2e/creature/level/1
  - pf2e/creature/trait/human
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/suli
  - pf2e/creature/trait/medium
statblock: inline
name: "Suli Dune Dancer"
level: 1
source: "Monster Core 2"
aon_id: "creature-4509"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4509"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Suli Dune Dancer"
level: "Creature 1"
size: "Medium"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: "Suli"
modifier: 5
perception:
  - name: "Perception"
    desc: "Perception +5"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Common|Common]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]], [[srd/pf2e/compendium/rules-elements/languages#Pyric|Pyric]], [[srd/pf2e/compendium/rules-elements/languages#Sussuran|Sussuran]], [[srd/pf2e/compendium/rules-elements/languages#Thalassic|Thalassic]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +5, [[srd/pf2e/compendium/rules-elements/skills/deception|Deception]] +6, [[srd/pf2e/compendium/rules-elements/skills/diplomacy|Diplomacy]] +7, [[srd/pf2e/compendium/rules-elements/skills/occultism|Occultism]] +4, [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] +7, [[srd/pf2e/compendium/rules-elements/skills/society|Society]] +4"
abilityMods: [2, 2, 0, 1, 0, 4]
abilities_top:
  - name: "Items"
    desc: "Scimitar, tambourine"
ac: 15
armorclass:
  - name: "AC"
    desc: "15; __Fort__: +3; __Ref__: +5; __Will__: +5"
hp: 16
health:
  - name: "HP"
    desc: "16"
abilities_mid:
  - name: "Elemental Bulwark"
    desc: "⬲"
  - name: "Trigger"
    desc: "An enemy is about to damage the dune dancer with cold, electricity, or fire, or with a spell that has the [[srd/pf2e/compendium/rules-elements/traits/player-core/air|air]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]], or [[srd/pf2e/compendium/rules-elements/traits/player-core/water|water]] trait"
  - name: "Effect"
    desc: "The dune dancer gain resistance 2 against the triggering damage."
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ scimitar +7 ([[srd/pf2e/compendium/rules-elements/traits/player-core/forceful|Forceful]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sweep|Sweep]]) __Damage__ 1d6+2 slashing"
abilities_bot:
  - name: "Distracting Dance"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/mental|Mental]], [[srd/pf2e/compendium/rules-elements/traits/player-core/visual|Visual]]) With a twirl of their body or with elaborate hand movements, the suli dune dancer attempts to distract a creature within 30 feet. The dune dance attempts a [[srd/pf2e/compendium/rules-elements/skills/performance|Performance]] check against the target's Perception DC."
  - name: "Critical Success"
    desc: "The target is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] and takes a –2 circumstance bonus to Perception checks until the end of the dune dancer's next turn."
  - name: "Success"
    desc: "The target is off-guard until the end of the dune dancer's current turn."
  - name: "Critical Failure"
    desc: "The dune dancer is off-guard against attacks from the target until the end of their next turn."
  - name: "Elemental Assault"
    desc: "⬺ Elemental magic fills the dune dancer's body or weapon. The dune dancer chooses one element and makes a melee Strike. The Strike deals an additional 1d4 damage of the indicated type and has the trait corresponding to the element:"
  - name: "Air"
    desc: "electricity"
  - name: "Earth"
    desc: "bludgeoning"
  - name: "Fire"
    desc: "fire"
  - name: "Metal"
    desc: "slashing"
  - name: "Water"
    desc: "cold"
  - name: "Wood"
    desc: "vitality"
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 17, attack +9 - __Cantrips (1st)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/guidance|Guidance]], [[srd/pf2e/compendium/spells/cantrips/shield|Shield]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-projectile|Telekinetic Projectile]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/dizzying-colors|Dizzying Colors]], [[srd/pf2e/compendium/spells/rank-1/soothe|Soothe]], [[srd/pf2e/compendium/spells/rank-1/sure-strike|Sure Strike]] (2 slots)"
sourcebook: "_Monster Core 2_, page 251."
```

```encounter-table
name: Suli Dune Dancer
creatures:
  - 1: Suli Dune Dancer
```
