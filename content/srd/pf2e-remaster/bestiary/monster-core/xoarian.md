---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Xoarian"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/aberration
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/small
statblock: inline
name: "Xoarian"
level: 8
source: "Monster Core"
aon_id: "creature-2929"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2929"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Xoarian"
level: "Creature 8"
size: "Small"
trait_01: "Aberration"
trait_02: "Uncommon"
modifier: 16
perception:
  - name: "Perception"
    desc: "Perception +16; thoughtsense 60 feet, tremorsense 60 feet"
languages: "Aklo; (can't speak any languages); telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Athletics +14, Deception +20, Diplomacy +16, Occultism +17, Society +17, Stealth +18"
abilityMods: [2, 4, 4, 5, 4, 6]
abilities_top:
  - name: "Stolen Identity"
    desc: "While a xoarian uses Body Thief, it gains the ability to understand and speak all languages known by the host, as well as knowledge of the host body's abilities, identity, role in society, and personality. However, it does not gain the specific memories or knowledge of the host body."
  - name: "Thoughtsense"
    desc: "The xoarian senses a creature's mental essence as a precise sense with the listed range; it cannot sense mindless creatures with thoughtsense."
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +14; __Ref__: +16; __Will__: +18"
hp: 130
health:
  - name: "HP"
    desc: "130; __Immunities__ blinded, controlled, emotion, possession"
speed: "35 feet, climb 20 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tentacle +18 (Agile, Finesse) __Damage__ 2d10+5 piercing"
abilities_bot:
  - name: "Body Thief"
    desc: "⬽ (Manipulate, Occult, Possession) The xoarian squeezes itself into the head of a creature dead no longer than a day, consuming and replacing that creature's brain. At the start of the xoarian's next turn, the body revives at its maximum Hit Points, controlled by the xoarian. The xoarian is conscious and can sense everything the possessed body could. Any effect that ends the possession kills the host body with the same effects as Exit Body. The xoarian can't use any of the host creature's spells with Body Thief but can use its own innate spells."
  - name: "Exit Body"
    desc: "⬻ (Move)"
  - name: "Requirements"
    desc: "The xoarian is controlling a body with Body Thief"
  - name: "Effect"
    desc: "The xoarian bursts out of its host body, which dies instantly and is no longer a suitable host for any Body Thief ability. The xoarian stretches to its full size in an adjacent space."
  - name: "Ravage"
    desc: "⬽ The xoarian makes two tentacle Strikes against a single paralyzed, restrained, or unconscious creature. If the target has 0 Hit Points after Ravage, the xoarian can use a free action with the death trait to kill the target and occupy it with Body Thief. Ilvarandin Eons ago, a group of xoarians discovered a vault in the Darklands that contained an already-abandoned city, Ilvarandin. They settled into the city while spreading rumors that Ilvarandin is a utopia where every day is lived in the pursuit of greater pleasure. Truthfully, these benefits only extend to the xoarians themselves. It's unknown what purpose, if any, the city serves in the Dominion's plans."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 27 - __Cantrips (4th)__ Daze, Detect Magic, Read Aura - __2nd__ Invisibility (at will; self only), Paranoia (at will) - __3rd__ Paralyze (×3), Soothe (×3) - __4th__ Confusion, Dispelling Globe"
sourcebook: "_Monster Core_, page 105."
```

```encounter-table
name: Xoarian
creatures:
  - 1: Xoarian
```
