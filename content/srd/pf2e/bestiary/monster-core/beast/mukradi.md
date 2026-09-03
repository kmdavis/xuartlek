---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Mukradi"
tags:
  - pf2e/creature/level/15
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Mukradi"
level: 15
source: "Monster Core"
aon_id: "creature-3100"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3100"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Mukradi"
level: "Creature 15"
size: "Gargantuan"
trait_01: "Beast"
modifier: 24
perception:
  - name: "Perception"
    desc: "Perception +24; darkvision, tremorsense (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +32"
abilityMods: [9, 0, 7, -3, 3, 0]
ac: 37
armorclass:
  - name: "AC"
    desc: "37; __Fort__: +32; __Ref__: +23; __Will__: +26"
hp: 300
health:
  - name: "HP"
    desc: "300; __Resistances__ [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] 20, [[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]] 20, [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] 20"
abilities_mid:
  - name: "Partitioned Anatomy"
    desc: "⭓"
  - name: "Trigger"
    desc: "The mukradi would be [[srd/pf2e/compendium/rules-elements/conditions#Confused|confused]], [[srd/pf2e/compendium/rules-elements/conditions#Paralyzed|paralyzed]], [[srd/pf2e/compendium/rules-elements/conditions#Slowed|slowed]], or [[srd/pf2e/compendium/rules-elements/conditions#Stunned|stunned]]"
  - name: "Effect"
    desc: "The mukradi confines the debilitating effect to a certain portion of its nervous system, ignoring the effect but causing a maw of its choice to go dormant for the effect's duration. That maw can't be used for a Strike or to Breathe Energy during that time. This ability can't be used if all the mukradi's heads are dormant."
  - name: "Spitting Rage"
    desc: "⬲"
  - name: "Trigger"
    desc: "A creature scores a critical hit on the mukradi"
  - name: "Effect"
    desc: "The mukradi's Breathe Energy recharges. It can use Breathe Energy immediately as part of this reaction. It can't use this reaction again until it recharges Breathe Energy naturally."
speed: "60 feet, burrow 60 feet, climb 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ acid maw +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d12+17 piercing plus 3d6 acid"
  - name: "Melee"
    desc: "⬻ flame maw +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d12+17 piercing plus 3d6 fire"
  - name: "Melee"
    desc: "⬻ shock maw +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 20 feet]]) __Damage__ 2d12+17 piercing plus 3d6 electricity"
  - name: "Melee"
    desc: "⬻ leg +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d10+17 piercing"
  - name: "Melee"
    desc: "⬻ tail lash +32 ([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 30 feet]]) __Damage__ 3d10+17 slashing plus Knockdown"
abilities_bot:
  - name: "Breathe Energy"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/primal|Primal]]) The mukradi breathes a blast of energy from one of its three heads; each creature in the area must attempt a DC 36 basic Reflex save. The mukradi can't Breathe Energy again for 1d4 rounds."
  - name: "Acid Maw"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]]) 10-foot-wide, 60-foot line of acid dealing 16d6 acid damage."
  - name: "Flame Maw"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]]) 60-foot cone of fire dealing 16d6 fire damage."
  - name: "Shock Maw"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/electricity|electricity]]) 120-foot line of electricity dealing 16d6 electricity damage."
  - name: "Pull Apart"
    desc: "⬺ The mukradi makes two Strikes with different maws against the same target. If both hit, the target takes an extra 2d12+13 slashing damage, with a DC 36 basic Fortitude save. On a critical failure, the creature is torn to pieces and dies. The mukradi's multiple attack penalty increases only after all the attacks are made."
  - name: "Thrash"
    desc: "⬺ The mukradi Strikes once against each creature in its reach. It can make one of these Strikes with each of its maws, one with its tail lash, and the rest with its legs. Each attack takes a –2 circumstance penalty and counts toward the mukradi's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks are made."
  - name: "Trample"
    desc: "⬽ Huge or smaller, leg, DC 36 From a God's Nightmares The first mukradis are rumored to have spawned in the fevered nightmares of a sleeping demigod from a dimension beyond dreams, who perished as the first mukradis hollowed out their unconscious mind and used their flesh to transition into the mortal realm. This legend is likely nothing more than fancy, but it certainly speaks to the deadly nature of these immense monsters."
sourcebook: "_Monster Core_, page 233."
```

```encounter-table
name: Mukradi
creatures:
  - 1: Mukradi
```
