---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Bythos"
tags:
  - pf2e/creature/level/16
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/large
statblock: inline
name: "Bythos"
level: 16
source: "Monster Core 2"
aon_id: "creature-4015"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4015"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Bythos"
level: "Creature 16"
size: "Large"
trait_01: "Aeon"
trait_02: "Monitor"
trait_03: "Uncommon"
modifier: 30
perception:
  - name: "Perception"
    desc: "Perception +30; darkvision"
languages: "envisioning"
skills:
  - name: "Skills"
    desc: "Athletics +32, Arcana +29, Deception +25, Intimidation +25, Nature +30, Occultism +29, Religion +30, Stealth +26"
abilityMods: [8, 4, 5, 7, 8, 5]
abilities_top:
  - name: "Envisioning"
    desc: "When a bythos conveys information, it does so wordlessly through psychic projections. This acts as telepathy with a range of 100 feet but is understandable to all creatures regardless of whether they have a language. The meaning to non-aeons can be vague and is often mysterious. A bythos can use this ability to communicate flawlessly with any other aeon on the same plane."
ac: 39
armorclass:
  - name: "AC"
    desc: "39; __Fort__: +25; __Ref__: +26; __Will__: +30 +1 status to all saves vs. magic"
hp: 245
health:
  - name: "HP"
    desc: "245 , regeneration 15 (deactivated by spirit); __Weaknesses__ spirit 15"
abilities_mid:
  - name: "Confusing Gaze"
    desc: "(aura, divine, emotion, incapacitation, mental, visual) 30 feet. A creature that ends its turn in the aura must attempt a DC 34 Will save. If it fails, it's confused for 1 round (or 1d4 rounds on a critical failure)."
  - name: "Temporal Reversion"
    desc: "⭓ (fortune)"
  - name: "Trigger"
    desc: "The bythos fails or critically fails a check"
  - name: "Frequency"
    desc: "once per day"
  - name: "Effect"
    desc: "The bythos rerolls the triggering check and takes the better result."
speed: "fly 35 feet"
attacks:
  - name: "Melee"
    desc: "⬻ fist +32 (Magical, reach 10 feet) __Damage__ 3d8+16 bludgeoning plus 2d8 cold"
abilities_bot:
  - name: "Aging Strikes"
    desc: "⬺ (Divine) The bythos make two fist Strikes against a single target. If both Strikes hit, the target attempts a DC 37 Fortitude save. Creatures that don't get weaker with age or don't age are immune (GM's discretion). If a creature becomes clumsy 4, drained 4, and enfeebled 4 due to Aging Strikes, it dies of old age."
  - name: "Success"
    desc: "The creature is unaffected."
  - name: "Failure"
    desc: "The creature becomes clumsy 1, drained 1, and enfeebled 1, or increases each of these conditions by 1. This effect is cumulative with other Aging Strikes from bythoses, to a maximum of clumsy 4, drained 4, and enfeebled 4."
  - name: "Critical Failure"
    desc: "As failure, but the creature becomes clumsy 2, drained 2, and enfeebled 2, or increases these conditions by 2."
  - name: "Focused Gaze"
    desc: "⬻ (Concentrate) The bythos focuses their gaze on a creature they can see within 30 feet. The target must attempt a save against the bythos's confusing gaze. A bythos can't use this ability against the same creature more than once per turn."
  - name: "Temporal Flurry"
    desc: "⬺ The bythos makes four fist Strikes. Their multiple attack penalty increases normally with each attack."
  - name: "Temporal Strike"
    desc: "⬺ (Divine, Incapacitation, Teleportation) The bythos touches a creature or object to displace it from time. The target attempts a DC 37 Fortitude save."
  - name: "Critical Success"
    desc: "The target is unaffected."
  - name: "Success"
    desc: "Time flows around the target; the target is slowed 1 for 1 round."
  - name: "Failure"
    desc: "The target disappears from the present moment and reappears in the same location 1d4 rounds later as if no time had passed for it. If a creature or object occupies that space when the target returns, the target appears in the closest available space to its original location."
  - name: "Critical Failure"
    desc: "As failure, but the target is slowed 1 for an extra 1d4 rounds after it returns. Guardians Of Time Bythos aeons have no innate ability to directly enter the mysterious Dimension of Time, but many know of the hidden routes in the Great Beyond one can use to travel to this strange realm. A bythos prefers to destroy those who seek entrance to the Dimension of Time rather than risk the knowledge of how to reach it spreading too far."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 37 - __4th__ Planar Tether (at will) - __6th__ Slow - __7th__ Haste, Interplanar Teleport, Planar Seal, Planar Tether - __8th__ Augury (at will), Teleport"
sourcebook: "_Monster Core 2_, page 12."
```

```encounter-table
name: Bythos
creatures:
  - 1: Bythos
```
