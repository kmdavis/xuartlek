---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Stargut Hydra"
tags:
  - pf2e/creature/level/9
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/large
statblock: inline
name: "Stargut Hydra"
level: 9
source: "Howl of the Wild"
aon_id: "creature-3293"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3293"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "HotW"
name: "Stargut Hydra"
level: "Creature 9"
size: "Large"
trait_01: "Beast"
modifier: 19
perception:
  - name: "Perception"
    desc: "Perception +19; scent (imprecise) 60 feet"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/athletics|Athletics]] +20, [[srd/pf2e/compendium/rules-elements/skills/stealth|Stealth]] +18, [[srd/pf2e/compendium/rules-elements/skills/survival|Survival]] +18"
abilityMods: [5, 3, 6, -3, 3, -1]
abilities_top:
  - name: "Skymetal Metamorphosis"
    desc: "(see sidebar)"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +21; __Ref__: +18; __Will__: +14"
hp: 150
health:
  - name: "HP"
    desc: "22 (head), head regrowth); __Immunities__ area damage; __Weaknesses__ slashing 10"
abilities_mid:
  - name: "Head Regrowth"
    desc: "A stargut hydra ordinarily has five heads. A creature can attempt to sever one of the hydra's heads by specifically targeting it and dealing damage equal to the head's Hit Points. A head that is not completely severed returns to full Hit Points at the end of any creature's turn. A hydra can regrow a severed head using hydra regeneration. A creature can prevent this regrowth by dealing acid or fire damage to the stump, cauterizing it. Single-target [[srd/pf2e/compendium/rules-elements/traits/player-core/acid|acid]] or [[srd/pf2e/compendium/rules-elements/traits/player-core/fire|fire]] effects need to be targeted at a specific stump, but effects that deal [[srd/pf2e/compendium/rules-elements/traits/gm-core/splash|splash]] damage or affect areas covering the hydra's whole space cauterize all stumps if they deal acid or fire damage. If the attack that severs a head deals any acid or fire damage, the stump is cauterized instantly. If all five heads are cauterized, the hydra dies."
  - name: "Hydra Regeneration"
    desc: "The stargut hydra has regeneration equal to 3 × the number of heads it has. If a hydra's body is missing any heads and the remaining stumps have not been cauterized, the hydra attempts a DC 29 Fortitude save after it regains Hit Points from regeneration. On a success, one uncauterized stump regrows two heads; on a critical success, two uncauterized stumps regrow into two heads each. The hydra can never grow more than double the number of heads it ordinarily has. The hydra's regeneration only fully deactivates if all its heads are severed and all stumps are cauterized, at which point it dies."
  - name: "Reactive Heads"
    desc: "A stargut hydra gains an extra reaction per round for each of its heads beyond the first, which it can use only to make Reactive Strikes. It can't use more than 1 reaction on the same triggering action, even if a creature leaves several squares within its reach, and the hydra must use a different head for each Reactive Strike it makes. Whenever one of the hydra's heads is severed, the hydra loses 1 of its extra reactions per round."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet, burrow 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaw +21 ([[srd/pf2e/compendium/rules-elements/traits/player-core/reach|reach 15 feet]]) __Damage__ 2d8+8 piercing"
abilities_bot:
  - name: "Vomit Meteorites"
    desc: "⬺ The stargut hydra lurches its entire body, spewing forth chunks of meteorite in a 30-foot cone that deal 5d6 bludgeoning damage to all creatures in the area (basic Reflex DC 25). The area becomes difficult terrain for 1 minute, though a creature can use an Interact action to clear one square of the rubble. The stargut hydra can't Vomit Meteorites for 1d4 rounds. Skymetal Metamorphosis Each stargut hydra has at least one metamorphosis resulting from consuming a specific skymetal and internalizing its properties. If you give a stargut hydra more than one metamorphosis, you should consider increasing its level and changing its statistics."
  - name: "Adamantine"
    desc: "The stargut hydra's Strikes bypass Hardness and are treated as adamantine. The stargut hydra gains resistance 10 to physical damage (except adamantine)."
  - name: "Abysium"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/poison|poison]]) The stargut hydra emits an aura of nauseating radiation from the abysium in its body. Any creature that begins its turn within 30 feet of the stargut hydra is [[srd/pf2e/compendium/rules-elements/conditions#Sickened|sickened 1]]."
  - name: "Djezet"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/magical|magical]]) The stargut hydra gains a +2 status bonus to saves against magic."
  - name: "Inubrix"
    desc: "The stargut hydra's Strikes ignore resistance to damage from metal armor's [[srd/pf2e/books/player-core/chapter-6-equipment/armor#Armor Specialization Effects|armor specialization effects]] and do not trigger the Shield Block reaction or reactions from armor property runes."
  - name: "Noqual"
    desc: "The stargut hydra's Strikes and abilities gain a +2 status bonus to damage against creatures with the ability to Cast a Spell."
  - name: "Orichalcum"
    desc: "When the stargut hydra has only two heads remaining, it is [[srd/pf2e/compendium/rules-elements/conditions#Quickened|quickened]]. It can use the extra action only to Stride or Strike."
  - name: "Siccatite"
    desc: "After the stargut hydra takes fire damage, it becomes superheated, gaining immunity to fire and weakness 10 to cold. While superheated, cold damage can be used to cauterize a stump. After the stargut hydra takes cold damage, it becomes chilled, gaining immunity to cold and weakness 10 to fire."
sourcebook: "_Howl of the Wild_, page 164."
```

```encounter-table
name: Stargut Hydra
creatures:
  - 1: Stargut Hydra
```
