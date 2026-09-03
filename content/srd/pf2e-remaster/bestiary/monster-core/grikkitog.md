---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Grikkitog"
tags:
  - pf2e/creature/level/14
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/earth
  - pf2e/creature/trait/huge
statblock: inline
name: "Grikkitog"
level: 14
source: "Monster Core"
aon_id: "creature-3035"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3035"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Grikkitog"
level: "Creature 14"
size: "Huge"
trait_01: "Aberration"
trait_02: "Earth"
modifier: 29
perception:
  - name: "Perception"
    desc: "Perception +29; darkvision, manifold vision, tremorsense (imprecise) 30 feet"
languages: "Petran"
skills:
  - name: "Skills"
    desc: "Athletics +28, Deception +27, Survival +25"
abilityMods: [8, 4, 5, 2, 5, 5]
abilities_top:
  - name: "Implant Core"
    desc: "⬽ (manipulate) The grikkitog implants its core into an adjacent section of earth or stone, melding seamlessly and changing its visual appearance to match the surrounding rock. It's immobilized but automatically succeeds at its Deception check to Impersonate the stone around it; creatures actively searching for it can still attempt Perception checks against its Deception DC as normal. A grikkitog can release its implantation as a free action, which has the manipulate trait. A grikkitog's infestation aura and manifold vision are only active while implanted."
  - name: "Manifold Vision"
    desc: "While its core is implanted, the grikkitog can see through the eyes it creates throughout the area of its infestation aura, gaining the benefits of all-around vision."
ac: 36
armorclass:
  - name: "AC"
    desc: "36; __Fort__: +28; __Ref__: +23; __Will__: +24"
hp: 200
health:
  - name: "HP"
    desc: "200; __Resistances__ 10 (except adamantine)"
abilities_mid:
  - name: "Infestation Aura"
    desc: "(aura, earth, occult) 120 feet. While its core is implanted, a grikkitog infests all earth and stone within 120 feet, as long as there is a contiguous physical connection between the earth, including stone objects touching the ground. This effect spreads even if the grikkitog does not have line of effect, though it can affect earth or stone on the surface and exposed to the air only if at least part of its core is exposed as well. Within the aura, it can grow maws and eyes everywhere. It can make jaws attacks against any creature, originating from any earth or stone in the aura adjacent to that creature. Determine cover from the origin point of the attack, not from the grikkitog's core."
speed: "20 feet; burrow 20 feet, earth glide"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +29 (Magical) __Damage__ 3d12+14 piercing plus barbed maw"
abilities_bot:
  - name: "Barbed Maw"
    desc: "⭓"
  - name: "Trigger"
    desc: "The grikkitog hits a creature with a jaws Strike"
  - name: "Effect"
    desc: "The grikkitog sinks its barbed teeth into the target, which must succeed at a DC 34 Reflex save or be immobilized. While immobilized, the victim takes 3d8 persistent bleed damage and the grikkitog feeds upon its flesh. The creature is immobilized until the grikkitog ends the effect as a free action or the target succeeds at a DC 38 check to Escape. The grikkitog can immobilize any number of creatures with these maws."
  - name: "Earth Glide"
    desc: "The grikkitog can Burrow through dirt and stone at its full burrow Speed, leaving no tunnels or signs of its passing. Grikkitog Origins Grikkitogs often feature as bogeymen in scary stories told by denizens of the Plane of Earth. Those who recall the wars between the elemental lords believe the first grikkitog was created as an experimental weapon by Ayrzul, the Fossilized King of the Elemental Plane of Earth. Yet the evil elemental lord did not realize the raw power of his creation. The grikkitog's hunger grew so ravenous that it escaped containment, infested an earth elemental warden, and began to spread across the planes. Now grikkitogs burrow throughout the Universe, devouring the unwary."
sourcebook: "_Monster Core_, page 183."
```

```encounter-table
name: Grikkitog
creatures:
  - 1: Grikkitog
```
