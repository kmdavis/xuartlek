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
languages: "Orvian, Petran; telepathy 300 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +39, Arcana +42, Architecture Lore +42, Athletics +39, Crafting +44, Engineering Lore +42, Nature +37, Planar Lore +42, Stealth +41, Thievery +39"
abilityMods: [8, 10, 7, 11, 6, 8]
abilities_top:
  - name: "Craft Crystal Wand"
    desc: "(exploration)"
  - name: "Frequency"
    desc: "twice per day"
  - name: "Effect"
    desc: "The vault builder spends 10 minutes creating a magic wand out of radioactive green crystal, containing any 8th-rank or lower earth spell of their choice. The wand can be used by other creatures, but it crumbles to sand at the end of the day and has no monetary value. The vault builder can expend both daily uses to instead make a _+3 greater striking major staff of earth_."
  - name: "Item Caster"
    desc: "The vault builder can Cast a Spell from any item (such as a staff or wand) as though it were on their spell list, but the spell can be 8th-rank or lower."
ac: 47
armorclass:
  - name: "AC"
    desc: "47; __Fort__: +36; __Ref__: +41; __Will__: +35 +1 status to all saves vs. spells ( +4 status vs. earth)"
hp: 465
health:
  - name: "HP"
    desc: "465; __Immunities__ bleed, paralyzed, poison, radiation, sleep; __Resistances__ physical 20 (except adamantine)"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "35 feet, burrow 25 feet, climb 35 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ crystal staff +39 (Magical, Radiation, two-hand d8) __Damage__ 4d4+12 bludgeoning plus 4d6 poison"
  - name: "Melee"
    desc: "⬻ crystal wand +37 (Finesse, Magical, Radiation) __Damage__ 4d4+12 piercing plus 4d6 poison"
  - name: "Melee"
    desc: "⬻ claw +37 (Agile, Finesse, Magical) __Damage__ 5d10+12 slashing plus constraining crystal"
  - name: "Ranged"
    desc: "⬻ crystal shard +37 (Earth, Finesse, Magical, range increment 100 feet) __Damage__ 7d6+4 piercing"
abilities_bot:
  - name: "Constraining Crystal"
    desc: "(Earth, Magical) When the vault builder deals damage with a claw Strike, glowing green crystals cluster at the site of the attack. The target must succeed at a DC 31 Fortitude save or become clumsy 1 for 1 hour (or clumsy 2 on a critical failure). If the creature is already clumsy due to constraining crystal, additional failures increase that clumsy value instead, to a maximum of clumsy 4. A target that fails its save while clumsy 4 is petrified with an unlimited duration."
  - name: "Crystal Burst"
    desc: "⬺ (Arcane, Earth) An explosion of razor-sharp splinters deals 24d6 piercing damage in a 30-foot burst within 120 feet, with a DC 46 basic Reflex save. The vault builder can't use Crystal Burst again for 1d4 rounds."
  - name: "Earth Glide"
    desc: "The vault builder can Burrow through any earthen matter, including rock. When they do so, the vault builder moves at their full burrow Speed, leaving no tunnels or signs of their passing."
spellcasting:
  - name: "Arcane Prepared Spells"
    desc: "DC 50, attack +42 - __Cantrips (10th)__ Detect Magic, Read Aura, Scatter Scree, Sigil, Telekinetic Hand - __1st__ Ant Haul, Quick Sort (×2) - __2nd__ Knock, Magnetic Attraction, Magnetic Repulsion - __3rd__ One with Stone (×2), Mending - __4th__ Clairvoyance, Engrave Memory, Grasping Earth - __5th__ Blazing Fissure, Creation, See the Unseen - __6th__ Pave Ground, Petrify, Wall of Force - __7th__ Fly, Haste (×2) - __8th__ Earthquake (×2), Mountain Resilience - __9th__ Disintegrate (×2), Heaving Earth"
  - name: "Arcane Innate Spells"
    desc: "DC 50, attack +42 - __4th__ Earthbind (at will), Shape Stone (at will), Translocate (at will) - __8th__ Petrify, Scrying, Shatter (at will), Speak with Stones (at will), Teleport, Translocate - __10th__ Summon Elemental (earth only), Wall of Stone"
sourcebook: "_Rage of Elements_, page 109."
```

```encounter-table
name: Vault Builder
creatures:
  - 1: Vault Builder
```
