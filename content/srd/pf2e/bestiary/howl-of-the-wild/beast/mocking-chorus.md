---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mocking Chorus"
tags:
  - pf2e/creature/level/18
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Mocking Chorus"
level: 18
source: "Howl of the Wild"
aon_id: "creature-3296"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3296"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Mocking Chorus"
level: "Creature 18"
size: "Large"
trait_01: "Beast"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; scent (imprecise) 60 feet"
languages: "all (see uncanny mimicry)"
skills:
  - name: "Skills"
    desc: "Athletics +35, Deception +36, Performance +35"
abilityMods: [9, 4, 6, -2, 2, 4]
abilities_top:
  - name: "Uncanny Mimicry"
    desc: "While unable to communicate for prolonged periods, a mocking chorus can precisely imitate a humanoid voice. If a creature speaks within audible range of the mocking chorus, the mocking chorus can speak using the creature's voice, even if it says different words than what were spoken. Creatures that hear the mocking chorus speak this way can attempt a DC 40 Will save to recognize the source. On a success, creatures gain a +1 circumstance bonus to all saving throws against the mocking chorus' abilities for 1 minute."
ac: 41
armorclass:
  - name: "AC"
    desc: "41; __Fort__: +33; __Ref__: +30; __Will__: +30"
hp: 340
health:
  - name: "HP"
    desc: "35 (head), head regrowth; __Immunities__ area damage"
abilities_mid:
  - name: "Weakness"
    desc: "slashing 10"
  - name: "Head Regrowth"
    desc: "A mocking chorus ordinarily has 10 heads. A creature can attempt to sever one of the hydra's heads by specifically targeting it and dealing damage equal to the head's Hit Points. A head that is not completely severed returns to full Hit Points at the end of any creature's turn. A hydra can regrow a severed head using hydra regeneration. A creature can prevent this regrowth by dealing acid or fire damage to the stump, cauterizing it. Single-target acid or fire effects need to be targeted at a specific stump, but effects that deal splash damage or affect areas covering the hydra's whole space cauterize all stumps if they deal acid or fire damage. If the attack that severs a head deals any acid or fire damage, the stump is cauterized instantly. If all five heads are cauterized, the hydra dies."
  - name: "Hydra Regeneration"
    desc: "The mocking chorus has regeneration equal to 3 × the number of heads it has. If a hydra's body is missing any heads and the remaining stumps have not been cauterized, the hydra attempts a DC 43 Fortitude save after it regains Hit Points from regeneration. On a success, one uncauterized stump regrows two heads; on a critical success, two uncauterized stumps regrow into two heads each. The hydra can never grow more than double the number of heads it ordinarily has. The hydra's regeneration only fully deactivates if all its heads are severed and all stumps are cauterized, at which point it dies."
  - name: "Reactive Heads"
    desc: "A mocking chorus gains an extra reaction per round for each of its heads beyond the first, which it can use only to make Reactive Strikes. It can't use more than 1 reaction on the same triggering action, even if a creature leaves several squares within its reach, and the hydra must use a different head for each Reactive Strike it makes. Whenever one of the hydra's heads is severed, the hydra loses 1 of its extra reactions per round."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "35 feet, swim 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +37 (reach 15 feet) __Damage__ 4d12+14 piercing"
  - name: "Ranged"
    desc: "⬻ harsh laugh +35 (Auditory, range increment 90 feet) __Damage__ 4d10+14 sonic"
abilities_bot:
  - name: "Petty Whispers"
    desc: "⬺ (Auditory, Mental) The mocking chorus adopts the voices of its enemies, spreading lies and jeers among would-be allies and tearing apart trusted friends. Creatures in a 60-foot emanation of the mocking chorus must attempt a DC 37 Will save. The mocking chorus can't use petty whispers again for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected and is temporarily immune for 1 day."
  - name: "Success"
    desc: "As failure, but the creature takes half damage and is not confused."
  - name: "Failure"
    desc: "The creature takes 12d10 mental damage and is confused for 1 minute. It can attempt a new save at the end of each of its turns to end the confusion."
  - name: "Critical Failure"
    desc: "The creature takes 15d10 damage and is confused for 1 minute, with no save to end early"
sourcebook: "_Howl of the Wild_, page 167."
```

```encounter-table
name: Mocking Chorus
creatures:
  - 1: Mocking Chorus
```
