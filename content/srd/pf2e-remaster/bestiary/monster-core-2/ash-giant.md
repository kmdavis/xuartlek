---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Ash Giant"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/giant
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Ash Giant"
level: 11
source: "Monster Core 2"
aon_id: "creature-4410"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4410"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Ash Giant"
level: "Creature 11"
size: "Large"
trait_01: "Giant"
trait_02: "Humanoid"
modifier: 21
perception:
  - name: "Perception"
    desc: "Perception +21; low-light vision"
languages: "Common, Jotun"
skills:
  - name: "Skills"
    desc: "Athletics +24, Crafting +16, Diplomacy +16, Intimidation +21, Survival +21"
abilityMods: [7, 3, 6, -1, 4, -2]
abilities_top:
  - name: "Vermin Empathy"
    desc: "The ash giant can ask questions of, receive answers from, and use the Diplomacy skill with insects, arachnids, and similar creatures."
  - name: "Items"
    desc: "piggy clod (6), _+1 striking war flail_"
ac: 30
armorclass:
  - name: "AC"
    desc: "30; __Fort__: +23; __Ref__: +18; __Will__: +21 +2 status to all saves vs. disease"
hp: 240
health:
  - name: "HP"
    desc: "240"
abilities_mid:
  - name: "Tumor Pop"
    desc: "When the ash giant takes piercing damage while they have a swollen tumor, the tumor explodes automatically, with the effect of Blastboil."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ war flail +25 (Disarm, magical, reach 10 feet, sweep, trip) __Damage__ 2d10+13 bludgeoning plus Gore Grinder"
  - name: "Melee"
    desc: "⬻ fist +24 (Agile, reach 10 feet, unarmed) __Damage__ 2d4+13 bludgeoning"
  - name: "Ranged"
    desc: "⬻ piggy clod +24 (Brutal, thrown 40 feet) __Damage__ 2d8+7 slashing plus 5 slashing splash damage"
abilities_bot:
  - name: "Blastboil"
    desc: "⬻ The ash giant pops one of the massive, swollen pustules on their body. Each creature in a 15-foot cone takes 5d8 poison damage with a DC 29 basic Reflex save. A creature that fails its save is also sickened 1 (or sickened 2 on a critical failure). This ability and tumor pop can't be used again until another tumor swells to a suitable size in 1d4 rounds."
  - name: "Gore Grinder"
    desc: "⬻"
  - name: "Requirements"
    desc: "The ash giant's last action was a successful war flail Strike"
  - name: "Effect"
    desc: "The ash giant wraps the chain of the flail around the target and grinds its flesh. The creature takes 2d10 slashing damage and 2d8 persistent bleed damage with a DC 30 basic Fortitude save."
  - name: "Tangle-Topple"
    desc: "⬺ The ash giant makes a piggy clod Strike. If it hits, the target is tangled in ragged scrap. It's immobilized, can't leave the ground, and falls to the ground if it's flying. This ends if the creature Escapes or the metal is Forced Open (DC 28). Chitinous Chariots Ash giants ride giant insects and other vermin to battle. They especially love to cover their mounts' exoskeletons with metal harnesses, armor plates, and jagged spikes added just for sadism's sake. Mounts they use frequently include the ankhrav hive mother and deadly mantis. Smaller creatures, including the narrik and the shriezyx, are harnessed into teams to pull forward their roving mechanisms of war."
sourcebook: "_Monster Core 2_, page 163."
```

```encounter-table
name: Ash Giant
creatures:
  - 1: Ash Giant
```
