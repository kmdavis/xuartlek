---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Xulgath Skulker"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/xulgath
  - pf2e/creature/trait/medium
statblock: inline
name: "Xulgath Skulker"
level: 2
source: "Monster Core"
aon_id: "creature-3245"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3245"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Xulgath Skulker"
level: "Creature 2"
size: "Medium"
trait_01: "Humanoid"
trait_02: "Xulgath"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Draconic|Draconic]], [[srd/pf2e/compendium/rules-elements/languages#Sakvroth|Sakvroth]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/acrobatics|Acrobatics]] +8, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +8, [[srd/pf2e/compendium/rules-elements/skills/thievery|Thievery]] +8"
abilityMods: [3, 4, 2, -1, 1, 0]
abilities_top:
  - name: "Items"
    desc: "Dagger (4)"
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +8; __Ref__: +10; __Will__: +5"
hp: 28
health:
  - name: "HP"
    desc: "28"
abilities_mid:
  - name: "Stench"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/olfactory|olfactory]]) 30 feet, DC 16"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+3 piercing"
  - name: "Melee"
    desc: "⬻ jaws +9 __Damage__ 1d6+3 piercing"
  - name: "Melee"
    desc: "⬻ claw +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/finesse|Finesse]]) __Damage__ 1d4+3 slashing"
  - name: "Ranged"
    desc: "⬻ dagger +10 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/thrown|thrown 10 feet]], [[srd/pf2e/compendium/rules-elements/traits/player-core/versatile|versatile S]]) __Damage__ 1d4+3 piercing"
abilities_bot:
  - name: "Hidden Movement"
    desc: "If a xulgath skulker starts their turn [[srd/pf2e/compendium/rules-elements/conditions#Undetected|undetected]] by a creature or merely [[srd/pf2e/compendium/rules-elements/conditions#Hidden|hidden]] from it, that creature is [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] against the skulker's attacks until the end of the skulker's turn."
  - name: "Mask Stench"
    desc: "⭓ The stalker masks their stench with curated herbs, suppressing their stench aura. The skulker can resume their stench aura as a free action."
  - name: "Sneak Attack"
    desc: "A xulgath skulker deals an additional 1d6 precision damage to [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]] creatures."
sourcebook: "_Monster Core_, page 353."
```

```encounter-table
name: Xulgath Skulker
creatures:
  - 1: Xulgath Skulker
```
