---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Akhana"
tags:
  - pf2e/creature/level/12
  - pf2e/creature/trait/aeon
  - pf2e/creature/trait/monitor
  - pf2e/creature/trait/medium
statblock: inline
name: "Akhana"
level: 12
source: "Monster Core"
aon_id: "creature-2799"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2799"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Akhana"
level: "Creature 12"
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
modifier: 27
perception:
  - name: "Perception"
    desc: "Perception +27; darkvision, lifesense 120 feet"
languages: "envisioning"
skills:
  - name: "Skills"
    desc: "Acrobatics +25, Athletics +24, Axis Lore +23, Medicine +23, Occultism +21, Religion +23"
abilityMods: [6, 6, 7, 3, 5, 4]
abilities_top:
  - name: "Envisioning"
    desc: "(aura, divine, mental) 100 feet. An akhana can communicate mentally with any creatures in the aura using wordless psychic projections. They don't need to share a language, though the aeon's meaning to non-aeons can be vague and is often mysterious. An aeon can use this ability to communicate flawlessly with any other aeon on the same plane as itself."
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +23; __Ref__: +22; __Will__: +23 +1 status to all saves vs. magical"
hp: 225
health:
  - name: "HP"
    desc: "225; __Immunities__ vitality, void; __Weaknesses__ spirit 10"
abilities_mid:
  - name: "Balance Life"
    desc: "⬲ (divine)"
  - name: "Trigger"
    desc: "A creature within 100 feet is about to attempt a recovery check"
  - name: "Effect"
    desc: "The akhana chooses to make the result a success or failure (but not a critical success or failure). This effect gains the fortune trait if the akhana chooses success or misfortune for failure."
speed: "fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +24 (Magical, Void) __Damage__ 5d10 void plus Grab"
  - name: "Melee"
    desc: "⬻ fist +24 (Agile, Magical) __Damage__ 3d6+12 bludgeoning plus 1d6 vitality or 1d6 void"
abilities_bot:
  - name: "Flying Fists"
    desc: "⬺ The akhana Flies and makes up to four fist Strikes against different targets at any points during this movement. The attacks count toward its multiple attack penalty normally, but the penalty does not increase until after Flying Fists is complete."
  - name: "Reclaim Life"
    desc: "⬻ (Divine, Void)"
  - name: "Requirements"
    desc: "The akhana has a living creature grappled or restrained with its tail"
  - name: "Effect"
    desc: "The creature takes 4d10 void damage with a DC 32 basic Fortitude save. On a failed save, it's also doomed 1. If the creature dies while doomed and held in the akhana's tail, its soul is trapped in the akhana (as _seize soul_), and its remains are preserved as peaceful rest. The soul returns to the body with 1 Hit Point if the akhana Dismisses the effect, if the akhana is slain, or if a _wish_ ritual or similarly powerful magic frees it."
  - name: "Sprout Life"
    desc: "⬺ (Concentrate, Divine, Plant, Vitality) A 5-foot burst within 100 feet fills with simple life appropriate to the environment. The newly forged animals bite those in the area for 7d6 piercing damage with a DC 32 basic Reflex save. The akhana can also have fungus or plants choke the area, even floating ones in the sky, creating difficult terrain. The created life lives or dies normally after its creation."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32 - __Cantrips (6th)__ Stabilize, Vitality Lash, Void Warp - __2nd__ Peaceful Rest (at will) - __4th__ Harm (at will), Heal (at will)"
sourcebook: "_Monster Core_, page 10."
```

```encounter-table
name: Akhana
creatures:
  - 1: Akhana
```
