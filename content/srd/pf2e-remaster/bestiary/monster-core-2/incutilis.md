---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Incutilis"
tags:
  - pf2e/creature/level/2
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/amphibious
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/tiny
statblock: inline
name: "Incutilis"
level: 2
source: "Monster Core 2"
aon_id: "creature-4446"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4446"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Incutilis"
level: "Creature 2"
size: "Tiny"
trait_01: "Aberration"
trait_02: "Amphibious"
trait_03: "Uncommon"
modifier: 7
perception:
  - name: "Perception"
    desc: "Perception +7; darkvision"
languages: "Aklo, Thalassic; telepathy 30 feet"
skills:
  - name: "Skills"
    desc: "Athletics +8, Deception +5, Stealth +9"
abilityMods: [4, 3, 1, 1, 3, -1]
ac: 17
armorclass:
  - name: "AC"
    desc: "17; __Fort__: +7; __Ref__: +7; __Will__: +9"
hp: 21
health:
  - name: "HP"
    desc: "21"
speed: "5 feet, climb 5 feet, swim 40 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +8 __Damage__ 1d4+4 bludgeoning plus Grab"
abilities_bot:
  - name: "Abandon Puppet"
    desc: "⬻ (Manipulate)"
  - name: "Requirements"
    desc: "The incutilis is attached to a puppet"
  - name: "Effect"
    desc: "The incutilis abandons its puppet, detaching and separating from its nervous system. If the puppet is still alive, it's unconscious and temporarily immune to that incutilis's Puppetmaster ability for 24 hours."
  - name: "Puppetmaster"
    desc: "⬽ (Manipulate) An incutilis drives tendrils into a Small or Medium living creature that's unconscious or restrained by the incutilis. They attach and inject the unfortunate host with enzymes to take over control of the creature's nervous system, turning the host into a puppet controlled by the incutilis. The puppet becomes controlled by the incutilis, and gains dying 2. This doesn't change the puppet's HP, and the puppet can have this dying condition even if it has more than 0 HP. If the puppet dies, its body remains under the control of the incutilis until it's destroyed or the incutilis Abandons the Puppet. If the puppet recovers from the dying condition, the incutilis immediately Abandons the Puppet. While controlling a puppet, the incutilis is attached to the puppet's head (or elsewhere, if its brain is in an unconventional location) and moves along with it. The puppet uses its own AC, Hit Points, Fortitude and Reflex saves, and physical Strikes, but it uses the incutilis's Will save. The puppet can perform only basic actions and untrained uses of the Athletics and Stealth skills while controlled. Any attack that deals damage to the puppet also deals 1 mental damage to the incutilis. Area effects are applied to both the incutilis and puppet. The incutilis always has lesser cover while in control of a puppet. Whalers' Tales The crews of whaling ships are among those most likely to encounter an incutilis. Whale brains aren't an incutilis's preferred food, but they can bore their tendrils into one for a long time. When such an unfortunate whale is brought alongside the whaling ship, an incutilis has an opportunity to climb aboard unseen and prey upon any member of the crew unlucky enough to be caught sleeping."
sourcebook: "_Monster Core 2_, page 198."
```

```encounter-table
name: Incutilis
creatures:
  - 1: Incutilis
```
