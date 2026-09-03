---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Prismhydra"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/rare
  - pf2e/creature/trait/huge
statblock: inline
name: "Prismhydra"
level: 16
source: "Howl of the Wild"
aon_id: "creature-3295"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3295"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Prismhydra"
level: "Creature 16"
size: "Huge"
trait_01: "Beast"
trait_02: "Rare"
modifier: 28
perception:
  - name: "Perception"
    desc: "Perception +28; scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +33, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +27, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +29"
abilityMods: [9, 6, 8, -3, 2, -1]
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +28; __Ref__: +26; __Will__: +24"
hp: 290
health:
  - name: "HP"
    desc: "36 (head), prismatic head regrowth; __Immunities__ area damage; __Weaknesses__ slashing 15)"
abilities_mid:
  - name: "Hydra Regeneration"
    desc: "The prismhydra has regeneration equal to 3 × the number of heads it has. If a hydra's body is missing any heads and the remaining stumps have not been cauterized, the hydra attempts a DC 39 Fortitude save after it regains Hit Points from regeneration. On a success, one uncauterized stump regrows two heads; on a critical success, two uncauterized stumps regrow into two heads each. The hydra can never grow more than double the number of heads it ordinarily has. The hydra's regeneration only fully deactivates if all its heads are severed and all stumps are cauterized, at which point it dies."
  - name: "Prismatic Head Regrowth"
    desc: "A prismhydra ordinarily has eight heads. A creature can attempt to sever one of the hydra's heads by specifically targeting it and dealing damage equal to the head's Hit Points. A head that is not completely severed returns to full Hit Points at the end of any creature's turn. A hydra can regrow a severed head using hydra regeneration. A creature can prevent this regrowth by dealing certain types of damage to the stump, cauterizing it. Single-target effects need to be targeted at a specific stump, but effects that deal [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage or affect areas covering the hydra's whole space cauterize all stumps if they deal the appropriate type of damage. If the attack that severs a head deals the appropriate type of damage, the stump is cauterized instantly. If all eight heads are cauterized, the hydra dies. Typically, two heads each are vulnerable to acid, cold, electricity, and fire damage, but other combinations or more exotic vulnerabilities are possible. When a prismhydra successfully regrows heads, all the heads regrown have the same vulnerability, which must be the same as the vulnerability of one of the prismhydra's unsevered heads."
  - name: "Prismatic Backlash"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature successfully cauterizes one of the prismhydra's stumps"
  - name: "Effect"
    desc: "The unstable prismatic energies in the prismhydra's body surge forth. Each creature adjacent to the prismhydra is exposed to its chromatic explosion (see below)."
  - name: "Reactive Heads"
    desc: "A prismhydra gains an extra reaction per round for each of its heads beyond the first, which it can use only to make Reactive Strikes. It can't use more than 1 reaction on the same triggering action, even if a creature leaves several squares within its reach, and the hydra must use a different head for each Reactive Strike it makes. Whenever one of the hydra's heads is severed, the hydra loses 1 of its extra reactions per round."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "35 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +31 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 3d12+14 piercing plus chromatic explosion"
  - name: "Ranged"
    desc: "⬻ spittle +28 ([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|Acid]], range increment 60 feet) __Damage__ 1d12 acid plus chromatic explosion"
abilities_bot:
  - name: "Chromatic Explosion"
    desc: "A prismhydra's heads are replete with arcane energy. Whenever the prismhydra successfully Strikes an opponent with its spittle, or when an opponent cauterizes one of the prismhydra's heads, the opponent takes 6d6 damage of the type matching the head's vulnerability (typically acid, cold, fire, or electricity), with a DC 37 basic Reflex save."
sourcebook: "_Howl of the Wild_, page 166."
```

```encounter-table
name: Prismhydra
creatures:
  - 1: Prismhydra
```
