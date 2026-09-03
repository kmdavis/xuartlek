---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Hydra"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/huge
statblock: inline
name: "Hydra"
level: 6
source: "Monster Core"
aon_id: "creature-3064"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3064"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Hydra"
level: "Creature 6"
size: "Huge"
trait_01: "Beast"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; low-light vision, scent (imprecise) 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +17, Stealth +12"
abilityMods: [7, 4, 5, -3, 2, -1]
ac: 23
armorclass:
  - name: "AC"
    desc: "23; __Fort__: +15; __Ref__: +12; __Will__: +10 all-around vision"
hp: 90
health:
  - name: "HP"
    desc: "(head) 15; __Immunities__ area damage; __Weaknesses__ slashing 5"
abilities_mid:
  - name: "Head Regrowth"
    desc: "A hydra ordinarily has five heads. A creature can attempt to sever one of the hydra's heads by specifically targeting it and dealing damage equal to the head's Hit Points. A head that is not completely severed returns to full Hit Points at the end of any creature's turn. A hydra can regrow a severed head using hydra regeneration. A creature can prevent this regrowth by dealing acid or fire damage to the stump, cauterizing it. Single-target acid or fire effects need to be targeted at a specific stump, but effects that deal splash damage or affect areas covering the hydra's whole space cauterize all stumps if they deal acid or fire damage. If the attack that severs a head deals any acid or fire damage, the stump is cauterized instantly. If all five heads are cauterized, the hydra dies."
  - name: "Hydra Regeneration"
    desc: "The hydra has regeneration equal to 3 × the number of heads it has. If a hydra's body is missing any heads and the remaining stumps have not been cauterized, the hydra attempts a DC 25 Fortitude save after it regains Hit Points from regeneration. On a success, one uncauterized stump regrows two heads; on a critical success, two uncauterized stumps regrow into two heads each. The hydra can never grow more than double the number of heads it ordinarily has. The hydra's regeneration only fully deactivates if all its heads are severed and all stumps are cauterized, at which point it dies."
  - name: "Reactive Heads"
    desc: "A hydra gains an extra reaction per round for each of its heads beyond the first, which it can use only to make Reactive Strikes. It can't use more than 1 reaction on the same triggering action, even if a creature leaves several squares within its reach, and the hydra must use a different head for each Reactive Strike it makes. Whenever one of the hydra's heads is severed, the hydra loses 1 of its extra reactions per round."
  - name: "Reactive Strike"
    desc: "⬲ (see reactive heads)"
speed: "25 feet, swim 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fangs +16 (reach 10 feet) __Damage__ 2d6+7 piercing"
abilities_bot:
  - name: "Focused Assault"
    desc: "⬺ The hydra attacks a single target with its heads, overwhelming its foe with multiple attacks and leaving almost nowhere to dodge. The hydra Strikes with its fangs. On a successful attack, the hydra deals damage from its fangs Strike to the target, plus an additional 1d6 damage for every head it has beyond the first. On a failure (but not a critical failure), the hydra deals the damage from one fangs Strike to the target creature. This Strike counts as a number of attacks equal to the number of heads the hydra has toward the hydra's multiple attack penalty."
  - name: "Storm of Jaws"
    desc: "⬺ The hydra makes a number of Strikes up to its number of heads, each against a different target. These attacks count toward the hydra's multiple attack penalty, but the multiple attack penalty doesn't increase until after the hydra makes all its attacks. Variant Hydras Scholars of bestial lore can describe several hydra variations. Though rare, hydras with more than five heads live in very isolated areas, sometimes guarding incredibly powerful artifacts. Legendary, 12-headed miasma hydras dwell in horribly polluted and dangerous swamps. Perhaps the most unexpected danger are newly hatched hydra larvae, born hungry in shallow bogs."
sourcebook: "_Monster Core_, page 204."
```

```encounter-table
name: Hydra
creatures:
  - 1: Hydra
```
