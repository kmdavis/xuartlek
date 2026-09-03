---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Kimenhul"
tags:
  - pf2e/creature/level/20
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/sahkil
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/huge
statblock: inline
name: "Kimenhul"
level: 20
source: "Monster Core 2"
aon_id: "creature-4538"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4538"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Kimenhul"
level: "Creature 20"
size: "Huge"
trait_01: "Fiend"
trait_02: "Sahkil"
trait_03: "Unholy"
modifier: 35
perception:
  - name: "Perception"
    desc: "Perception +35; darkvision, _truesight_"
languages: "Chthonian, Diabolic, Empyrean, Requian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +36, Arcana +33, Athletics +34, Deception +38, Occultism +33, Religion +35, Stealth +36"
abilityMods: [10, 8, 9, 5, 7, 7]
abilities_top:
  - name: "Easy to Call"
    desc: "A sahkil's level is considered 2 lower for the purpose of being conjured by the _binding circle_ ritual (and potentially other rituals, at the GM's discretion), but it's always free to attack or leave instead of negotiate unless the primary caster's check is a critical success."
ac: 45
armorclass:
  - name: "AC"
    desc: "45; __Fort__: +33; __Ref__: +32; __Will__: +35 +4 status bonus vs. mental effects"
hp: 425
health:
  - name: "HP"
    desc: "425; __Immunities__ death effects, fear; __Weaknesses__ holy 20"
abilities_mid:
  - name: "Feed on Fear"
    desc: "The kimenhul regains 30 Hit Points at the start of its turn as long as any frightened creature is within 100 feet of it."
  - name: "Reactive Strike"
    desc: "⬲ If the triggering creature is frightened, the kimenhul can make two claw Strikes against the creature instead of one Strike."
speed: "45 feet, climb 25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +38 (Magical, reach 15 feet, unholy) __Damage__ 4d12+18 piercing plus 3d6 spirit"
  - name: "Melee"
    desc: "⬻ claw +38 (Agile, magical, reach 15 feet, unholy) __Damage__ 4d8+18 slashing plus 3d6 spirit and Improved Grab"
abilities_bot:
  - name: "Eternal Fear"
    desc: "⬺ (Divine, emotion, fear, incapacitation, Mental) The kimenhul contorts its faces and presents itself to its enemies in a terrifying and traumatic display that causes lingering fear. Each creature within 100 feet that can observe the kimenhul must attempt a DC 42 Will save. They are then temporarily immune for 10 minutes."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "The target becomes frightened 3."
  - name: "Failure"
    desc: "The target becomes frightened 3 and is fleeing as long as it’s frightened. Even after recovering from the initial experience, the trauma is lodged in the target’s mind for 1 year. Once per day, the kimenhul can communicate telepathically with the target for 1 minute as long as both creatures are on the same plane. Any time a creature under the effect of Eternal Fear is in a stressful situation (such as combat or intense social pressure), they must succeed at a DC 11 flat check or become frightened 2. While Eternal Fear lasts, the target always becomes fleeing as long as it’s frightened, regardless of the source of the fear. The target can attempt a new saving throw each week to remove these effects, but they can otherwise be removed by only powerful magic such as a _wish_ ritual."
  - name: "Critical Failure"
    desc: "As failure, but the effects are permanent, and the target doesn’t get to attempt a weekly save to end the effect."
  - name: "Frightening Flurry"
    desc: "⬺ The kimenhul makes one jaws Strike and two claw Strikes against a single target, in any order. The target becomes frightened with a condition value equal to the number of Strikes that hit it, to a maximum of frightened 3 if all three Strikes hit."
  - name: "Rend"
    desc: "⬻ claw"
  - name: "Skip Between"
    desc: "⬻ (Divine, Teleportation) The sahkil moves from the Universe to the Ethereal Plane or vice-versa. While in the Ethereal Plane, they're unable to affect anything in the Universe, and they cannot be seen by beings or abilities in the Universe, unless these have an ability that can gaze into the Ethereal Plane. While on the Material Plane the inverse is true for anything on the Ethereal Plane. A summoned sahkil can't use Skip Between."
  - name: "Snatch Between"
    desc: "When using Skip Between, the kimenhul can bring along any creatures it has grabbed."
  - name: "Unsettled Mind"
    desc: "Any creature affected by any of a kimenhul's mental spells or abilities becomes stupefied 3 for the duration of that effect and for 1d4 rounds thereafter."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 42 - __Cantrips (10th)__ Detect Magic - __9th__ Confusion, Dispel Magic (at will), Fear (at will), Mask of Terror (at will), Phantasmagoria, Phantasmal Calamity, Suggestion (at will), Warp Mind - __Constant (9th)__ Hidden Mind, Truesight"
sourcebook: "_Monster Core 2_, page 278."
```

```encounter-table
name: Kimenhul
creatures:
  - 1: Kimenhul
```
