---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Volnagur"
tags:
  - pf2e/creature/level/22
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/unique
  - pf2e/creature/trait/gargantuan
statblock: inline
name: "Volnagur"
level: 22
source: "Monster Core 2"
aon_id: "creature-4559"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4559"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Volnagur"
level: "Creature 22"
size: "Gargantuan"
trait_01: "Beast"
trait_02: "Unique"
modifier: 39
perception:
  - name: "Perception"
    desc: "Perception +39; darkvision"
languages: "Aklo; (can't speak any language)"
skills:
  - name: "Skills"
    desc: "Athletics +42, Performance +45"
abilityMods: [9, 11, 11, -2, 3, 7]
abilities_top:
  - name: "Slumbering Armageddon"
    desc: "Volnagur's slumber increases the rate of wildlife attacks, swarms of vermin and pests, and violent crime."
ac: 48
armorclass:
  - name: "AC"
    desc: "48; __Fort__: +39; __Ref__: +36; __Will__: +33"
hp: 515
health:
  - name: "HP"
    desc: "515 , regeneration absolute 25; __Immunities__ clumsy, disease, drained, enfeebled, mental, paralyzed, petrified, poison, polymorph, sonic, stupefied"
abilities_mid:
  - name: "Absolute Regeneration"
    desc: "Volnagur's regeneration can be deactivated if a choir of no less than 12 exquisitely skilled and inspired individuals sings a song of beginnings and hope over its corpse for 1 year and 1 day without pause or flaw."
  - name: "Alien Harmonics"
    desc: "(auditory, aura, sonic) 60 feet. Volnagur constantly emits a cacophony that drowns out sound and thought while reinforcing Volnagur's song. Creatures that enter the aura must attempt a DC 43 Fortitude save or Volnagur's song becomes all they can hear for as long as they remain within the aura, making creatures deafened against all sources other than Volnagur. On a critical failure, the effect is permanent, and the cacophony rings in the target's ears regardless of range. The aura also attempts to counteract any auditory effect, any effect that would provide resistance or immunity to auditory or sonic effects, or any effect that would create silence (counteract rank 10, counteract modifier +33)."
  - name: "Frightful Presence"
    desc: "(aura, emotion, fear, mental) 300 feet, DC 42"
  - name: "Reactive"
    desc: "Volnagur gains 3 reactions each round. It can still use only one reaction per trigger"
  - name: "Intercepting Eyes"
    desc: "⬲"
  - name: "Trigger"
    desc: "Volnagur is targeted by a ranged attack"
  - name: "Requirements"
    desc: "Volnagur is aware of the attack and not off-guard to it"
  - name: "Effect"
    desc: "One of Volnagur's eyes fixes on the attack, shooting it down with an eye beam. The attack becomes a critical failure."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "20 feet, fly 80 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +41 (Finesse, reach 20 feet) __Damage__ 4d10+24 piercing plus endsong and Grab"
  - name: "Melee"
    desc: "⬻ razor tongues +41 (Finesse, reach 40 feet) __Damage__ 4d8+24 slashing plus endsong and Grab"
  - name: "Ranged"
    desc: "⬻ eye beam +41 (Magical, range increment 120 feet, sonic) __Damage__ 6d12 sonic plus endsong"
abilities_bot:
  - name: "Endsong"
    desc: "(Curse, mental, sonic) Subtle vibrations laced under Volnagur's attacks confuse its targets and fill their minds with the desire to destroy. A creature damaged by one of Volnagur's Strikes must attempt a DC 45 Will save."
  - name: "Critical Success"
    desc: "The target is unaffected and is temporarily immune for 24 hours or until it takes damage from Scream of the End."
  - name: "Success"
    desc: "The target is unaffected."
  - name: "Failure"
    desc: "The target is confused for 1d4 rounds. It never attempts to attack Volnagur or another creature affected by endsong."
  - name: "Critical Failure"
    desc: "As failure, but the target is confused for 1 hour. While confused, its Strikes resonate with Volnagur's song, dealing an additional 1d6 sonic damage and forcing the target to save against endsong."
  - name: "Gaze Upon"
    desc: "⬺ Volnagur makes an eye beam Strike against every creature in a 120-foot cone. These attacks count toward Volnagur's multiple attack penalty, but the multiple attack penalty doesn't increase until after Volnagur makes all its attacks. It can't use Gaze Upon again for 1d4 rounds, but until the start of Volnagur's next turn, it can use Intercepting Eyes as a free action."
  - name: "Scream of the End"
    desc: "⬺ (Sonic)"
  - name: "Requirements"
    desc: "Volnagur has a creature grabbed or restrained"
  - name: "Effect"
    desc: "Volnagur holds a creature close to its eyes before blasting the creature at point-blank range. Volnagur deals 23d6 sonic damage to the target (DC 46 basic Reflex save). Regardless of the save's result, the target is no longer grabbed or restrained, is pushed 120 feet away from Volnagur, and falls prone."
sourcebook: "_Monster Core 2_, page 299."
```

```encounter-table
name: Volnagur
creatures:
  - 1: Volnagur
```
