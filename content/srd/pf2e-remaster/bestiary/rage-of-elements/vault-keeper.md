---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Vault Keeper"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/medium
statblock: inline
name: "Vault Keeper"
level: 14
source: "Rage of Elements"
aon_id: "creature-2629"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2629"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "RoE"
name: "Vault Keeper"
level: "Creature 14"
size: "Medium"
trait_01: "Earth"
trait_02: "Elemental"
trait_03: "Rare"
modifier: 26
perception:
  - name: "Perception"
    desc: "Perception +26; darkvision, tremorsense (imprecise) 120 feet"
languages: "Orvian, Petran; telepathy 300 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +26, Arcana +26, Athletics +26, Crafting +26, Nature +24, Planar Lore +28, Thievery +24"
abilityMods: [4, 8, 6, 8, 4, 6]
abilities_top:
  - name: "Craft Crystal Wand"
    desc: "(exploration)"
  - name: "Frequency"
    desc: "twice per day"
  - name: "Effect"
    desc: "The vault keeper spends 10 minutes creating a magic wand out of radioactive green crystal, containing any 5th-rank or lower earth spell of their choice. The wand can be used by other creatures, but it crumbles to sand at the end of the day and has no monetary value."
  - name: "Item Caster"
    desc: "The vault keeper can Cast a Spell from any item (such as a staff or wand) as though it were on their spell list."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +24; __Ref__: +28; __Will__: +22"
hp: 200
health:
  - name: "HP"
    desc: "200; __Immunities__ bleed, paralyzed, poison, radiation, sleep; __Resistances__ physical 15 (except adamantine)"
abilities_mid:
  - name: "Reactive Strike"
    desc: "⬲"
speed: "35 feet, climb 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ claw +28 (Agile, Finesse, Magical) __Damage__ 3d10+10 slashing plus constraining crystal"
  - name: "Melee"
    desc: "⬻ crystal wand +28 (Finesse, Magical, Radiation) __Damage__ 3d4+10 piercing plus 4d6 poison"
  - name: "Ranged"
    desc: "⬻ crystal shard +28 (Earth, Magical, range increment 100 feet) __Damage__ 5d6+6 piercing"
abilities_bot:
  - name: "Constraining Crystal"
    desc: "(Earth, Magical) When the vault keeper deals damage with a claw Strike, glowing green crystals cluster at the site of the attack. The target must succeed at a DC 31 Fortitude save or become clumsy 1 for 1 hour (or clumsy 2 on a critical failure). If the creature is already clumsy due to constraining crystal, additional failures increase that clumsy value instead, to a maximum of clumsy 4."
  - name: "Crystal Burst"
    desc: "⬺ (Arcane, Earth) An explosion of razor-sharp splinters deals 15d6 piercing damage in a 30-foot burst within 120 feet, with a DC 35 basic Reflex save. The vault keeper can't use Crystal Burst again for 1d4 rounds."
  - name: "Slashing Surge"
    desc: "⬺ The vault keeper Strides or Climbs and makes two claw Strikes at any point during that movement. Each Strike must target a different creature. The multiple attack penalty doesn't increase until after both attacks."
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 34, attack +26 - __4th__ Earthbind (at will), Shape Stone (at will), Translocate (at will) - __5th__ Shatter (at will), Translocate - __6th__ Scrying, Speak with Stones (at will) - __7th__ Petrify, Summon Elemental (earth only), Wall of Stone"
sourcebook: "_Rage of Elements_, page 108."
```

```encounter-table
name: Vault Keeper
creatures:
  - 1: Vault Keeper
```
