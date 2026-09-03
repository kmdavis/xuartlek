---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Doldrums Heap"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/plant
  - pf2e/creature/trait/huge
statblock: inline
name: "Doldrums Heap"
level: 9
source: "Monster Core"
aon_id: "creature-3172"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3172"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Doldrums Heap"
level: "Creature 9"
size: "Huge"
trait_01: "Amphibious"
trait_02: "Plant"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; wavesense (precise) 120 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +21, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18"
abilityMods: [6, 4, 5, -4, 2, 0]
ac: 16
armorclass:
  - name: "AC"
    desc: "16; __Fort__: +21; __Ref__: +18; __Will__: +15"
hp: 300
health:
  - name: "HP"
    desc: "300; __Immunities__ critical hits, [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]], precision, [[srd/pf2e/compendium/rules-elements/conditions#Unconscious|unconscious]]; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/cold|cold]] 10; __Weaknesses__ slashing 10"
abilities_mid:
  - name: "Mirage Spores"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/incapacitation|incapacitation]], [[srd/pf2e/compendium/rules-elements/traits/player-core/mental|mental]]) 300 feet. The doldrums heap constantly produces a field of hallucinogenic spores that causes those affected to see the monster as whatever they desire most. Each creature within the emanation must succeed a DC 27 Will save or become [[srd/pf2e/compendium/rules-elements/conditions#Fascinated|fascinated]] with the doldrums heap and compelled to move toward it on the creature's turn. Creatures fascinated this way are also [[srd/pf2e/compendium/rules-elements/conditions#Off-Guard|off-guard]]. If the doldrums heap attacks, the fascinated condition ends only for the creature that is attacked. On a successful save, a creature is temporarily immune to mirage spores for 24 hours."
speed: "20 feet, climb 20 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tendril +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d12+10 bludgeoning plus Grab"
abilities_bot:
  - name: "Constrict"
    desc: "⬻ 1d12+10 bludgeoning, DC 28"
  - name: "Draw In"
    desc: "⬺ The doldrums heap attempts to [[srd/pf2e/compendium/rules-elements/actions/player-core#Reposition|Reposition]] up to three creatures it has [[srd/pf2e/compendium/rules-elements/conditions#Grabbed|grabbed]] or [[srd/pf2e/compendium/rules-elements/conditions#Restrained|restrained]]. These attempts neither apply nor count toward the heap's multiple attack penalty. It can move them into its own space, dealing 1d12+10 bludgeoning damage."
sourcebook: "_Monster Core_, page 295."
```

```encounter-table
name: Doldrums Heap
creatures:
  - 1: Doldrums Heap
```
