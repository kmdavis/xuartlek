---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Elemental Avalanche"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/elemental
  - pf2e/creature/trait/huge
statblock: inline
name: "Elemental Avalanche"
level: 11
source: "Monster Core"
aon_id: "creature-2980"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2980"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Elemental Avalanche"
level: "Creature 11"
size: "Huge"
trait_01: "Earth"
trait_02: "Elemental"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision, tremorsense (imprecise) 90 feet"
languages: "[[srd/pf2e/compendium/rules-elements/languages#Petran|Petran]]"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +24, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +14"
abilityMods: [7, -1, 8, 0, 3, -1]
abilities_top:
  - name: "Earthbound"
    desc: "When not touching solid ground, the elemental avalanche is [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed 1]], can't use reactions, and can't Trample."
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +26; __Ref__: +17; __Will__: +21"
hp: 215
health:
  - name: "HP"
    desc: "215; __Immunities__ bleed, [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]], [[srd/pf2e/compendium/rules-elements/traits/player-core/sleep|sleep]]"
abilities_mid:
  - name: "Spike Stones"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]], [[srd/pf2e/compendium/rules-elements/traits/player-core/primal|primal]]) 5 feet. Spikes of rock rise up from all stone surfaces in the emanation, creating difficult terrain. A creature moving in the terrain takes 2d8 piercing damage for each square of spikes it moves into (a Large or larger creature takes damage only once for each square it moves, even if its space covers multiple squares of spikes). Creatures with the [[srd/pf2e/compendium/rules-elements/traits/player-core/earth|earth]] trait ignore all effects within the area. The living avalanche can disable or activate this aura using a single action, which has the [[srd/pf2e/compendium/rules-elements/traits/player-core/concentrate|concentrate]] trait."
  - name: "Crumble"
    desc: "⬲ Trigger The living avalanche takes damage from a hostile source while atop rock or earth; Effect The living avalanche crumbles into the ground, [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrowing]]down 20 feet. This Burrowing does not trigger reactions. The living avalanche can't Crumble again for 1d4 rounds"
speed: "25 feet, burrow 25 feet; earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d12+11 bludgeoning plus Knockdown"
  - name: "Ranged"
    desc: "⬻ rock +24 (Brutal, range increment 80 feet) __Damage__ 2d12+7 bludgeoning"
abilities_bot:
  - name: "Earth Glide"
    desc: "The living avalanche can [[srd/pf2e/compendium/rules-elements/actions/player-core#Burrow|Burrow]] through any earthen matter, including rock. When it does so, the living avalanche moves at its full burrow Speed, leaving no tunnels or signs of its passing."
  - name: "Grinding Stones"
    desc: "⬺ The elemental avalanche deals 4d12 bludgeoning damage to each [[srd/pf2e/compendium/rules-elements/conditions#Prone|prone]] creature within the elemental's melee reach with a DC 30 basic Reflex save."
  - name: "Trample"
    desc: "⬽ Large or smaller, fist, DC 30"
sourcebook: "_Monster Core_, page 143."
```

```encounter-table
name: Elemental Avalanche
creatures:
  - 1: Elemental Avalanche
```
