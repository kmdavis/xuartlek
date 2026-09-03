---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vault Builder"
tags:
  - pf2e/creature/level/23
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Vault Builder"
level: 23
source: "Rage of Elements"
aon_id: "creature-2630"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2630"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Vault Builder"
level: "Creature 23"
size: "Medium"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: "Rare"
modifier: 37
perception:
  - name: "Perception"
    desc: "Perception +37; darkvision, tremorsense (imprecise) 120 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Orvian|Orvian]], [[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]; telepathy 300 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +39, [[srd/pf2e/compendium/rules-elements/skills/arcana|Arcana]] +42, Architecture Lore +42, [[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +39, [[srd/pf2e/compendium/rules-elements/skills/crafting|Crafting]] +44, Engineering Lore +42, [[srd/pf2e/compendium/rules-elements/skills/nature|Nature]] +37, Planar Lore +42, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +41, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +39"
abilityMods: [8, 10, 7, 11, 6, 8]
abilities_top:
  - name: "Craft Crystal Wand"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/exploration|exploration]])"
  - name: "Frequency"
    desc: "twice per day"
  - name: "Effect"
    desc: "The vault builder spends 10 minutes creating a magic wand out of radioactive green crystal, containing any 8th-rank or lower [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]] spell of their choice. The wand can be used by other creatures, but it crumbles to sand at the end of the day and has no monetary value. The vault builder can expend both daily uses to instead make a _+3 greater striking [[srd/pf2e/compendium/equipment/staves/staff-of-earth-major|major staff of earth]]_."
  - name: "Item Caster"
    desc: "The vault builder can Cast a Spell from any item (such as a staff or wand) as though it were on their spell list, but the spell can be 8th-rank or lower."
ac: 47
armorclass:
  - name: "AC"
    desc: "47; __Fort__: +36; __Ref__: +41; __Will__: +35 +1 status to all saves vs. spells ( +4 status vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]])"
hp: 465
health:
  - name: "HP"
    desc: "465; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], radiation, [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]; __Resistances__ physical 20 (except adamantine)"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "35 feet, burrow 25 feet, climb 35 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ crystal staff +39 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], Radiation, [[srd/pf2e/compendium/rules-elements/traits/player-core/two-hand|two-hand d8]]) __Damage__ 4d4+12 bludgeoning plus 4d6 poison"
  - name: "Melee"
    desc: "⬻ crystal wand +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], Radiation) __Damage__ 4d4+12 piercing plus 4d6 poison"
  - name: "Melee"
    desc: "⬻ claw +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) __Damage__ 5d10+12 slashing plus constraining crystal"
  - name: "Ranged"
    desc: "⬻ crystal shard +37 ([[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], range increment 100 feet) __Damage__ 7d6+4 piercing"
abilities_bot:
  - name: "Constraining Crystal"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]]) When the vault builder deals damage with a claw Strike, glowing green crystals cluster at the site of the attack. The target must succeed at a DC 31 Fortitude save or become clumsy 1 for 1 hour (or clumsy 2 on a critical failure). If the creature is already clumsy due to constraining crystal, additional failures increase that clumsy value instead, to a maximum of clumsy 4. A target that fails its save while clumsy 4 is [[srd/pf2e/compendium/rules-elements/conditions#Petrified|petrified]] with an unlimited duration."
  - name: "Crystal Burst"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/arcane|Arcane]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|Earth]]) An explosion of razor-sharp splinters deals 24d6 piercing damage in a 30-foot burst within 120 feet, with a DC 46 basic Reflex save. The vault builder can't use Crystal Burst again for 1d4 rounds."
  - name: "Earth Glide"
    desc: "The vault builder can Burrow through any earthen matter, including rock. When they do so, the vault builder moves at their full burrow Speed, leaving no tunnels or signs of their passing."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 50, attack +42 - __Cantrips (10th)__ [[srd/pf2e/compendium/spells/cantrips/detect-magic|Detect Magic]], [[srd/pf2e/compendium/spells/cantrips/read-aura|Read Aura]], [[srd/pf2e/compendium/spells/cantrips/scatter-scree|Scatter Scree]], [[srd/pf2e/compendium/spells/cantrips/sigil|Sigil]], [[srd/pf2e/compendium/spells/cantrips/telekinetic-hand|Telekinetic Hand]] - __1st__ [[srd/pf2e/compendium/spells/rank-1/ant-haul|Ant Haul]], Quick Sort (×2) - __2nd__ [[srd/pf2e/compendium/spells/rank-2/knock|Knock]], Magnetic Attraction, Magnetic Repulsion - __3rd__ [[srd/pf2e/compendium/spells/rank-3/one-with-stone|One with Stone]] (×2), [[srd/pf2e/compendium/spells/rank-1/mending|Mending]] - __4th__ [[srd/pf2e/compendium/spells/rank-4/clairvoyance|Clairvoyance]], [[srd/pf2e/compendium/spells/rank-5/engrave-memory|Engrave Memory]], [[srd/pf2e/compendium/spells/rank-4/grasping-earth|Grasping Earth]] - __5th__ Blazing Fissure, [[srd/pf2e/compendium/spells/rank-4/creation|Creation]], [[srd/pf2e/compendium/spells/rank-2/see-the-unseen|See the Unseen]] - __6th__ [[srd/pf2e/compendium/spells/rank-2/pave-ground|Pave Ground]], [[srd/pf2e/compendium/spells/rank-6/petrify|Petrify]], [[srd/pf2e/compendium/spells/rank-6/wall-of-force|Wall of Force]] - __7th__ [[srd/pf2e/compendium/spells/rank-4/fly|Fly]], [[srd/pf2e/compendium/spells/rank-3/haste|Haste]] (×2) - __8th__ [[srd/pf2e/compendium/spells/rank-8/earthquake|Earthquake]] (×2), [[srd/pf2e/compendium/spells/rank-4/mountain-resilience|Mountain Resilience]] - __9th__ [[srd/pf2e/compendium/spells/rank-6/disintegrate|Disintegrate]] (×2), [[srd/pf2e/compendium/spells/rank-7/heaving-earth|Heaving Earth]]"
  - name: "Arcane Innate Spells"
    desc: "DC 50, attack +42 - __4th__ [[srd/pf2e/compendium/spells/rank-3/earthbind|Earthbind]] (at will), [[srd/pf2e/compendium/spells/rank-4/shape-stone|Shape Stone]] (at will), [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] (at will) - __8th__ [[srd/pf2e/compendium/spells/rank-6/petrify|Petrify]], [[srd/pf2e/compendium/spells/rank-6/scrying|Scrying]], [[srd/pf2e/compendium/spells/rank-2/shatter|Shatter]] (at will), [[srd/pf2e/compendium/spells/rank-5/speak-with-stones|Speak with Stones]] (at will), [[srd/pf2e/compendium/spells/rank-6/teleport|Teleport]], [[srd/pf2e/compendium/spells/rank-4/translocate|Translocate]] - __10th__ [[srd/pf2e/compendium/spells/rank-2/summon-elemental|Summon Elemental]] (earth only), [[srd/pf2e/compendium/spells/rank-5/wall-of-stone|Wall of Stone]]"
sourcebook: "_Rage of Elements_, page 109."
```

```encounter-table
name: Vault Builder
creatures:
  - 1: Vault Builder
```
