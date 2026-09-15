---
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
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=2799"
socialImage: og-image.png
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
    desc: "+27; darkvision, lifesense 120 feet"
languages: "envisioning"
skills:
  - name: "Skills"
    desc: "[[srd/pf2e/compendium/rules-elements/skills/Acrobatics|Acrobatics]] +25, [[srd/pf2e/compendium/rules-elements/skills/Athletics|Athletics]] +24, Axis Lore +23, [[srd/pf2e/compendium/rules-elements/skills/Medicine|Medicine]] +23, [[srd/pf2e/compendium/rules-elements/skills/Occultism|Occultism]] +21, [[srd/pf2e/compendium/rules-elements/skills/Religion|Religion]] +23"
abilityMods: [6, 6, 7, 3, 5, 4]
abilities_top:
  - name: "Envisioning"
    desc: "([[srd/pf2e/compendium/rules-elements/traits/player-core/Aura|aura]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Mental|mental]]) 100 feet. An akhana can communicate mentally with any creatures in the aura using wordless psychic projections. They don't need to share a language, though the aeon's meaning to non-aeons can be vague and is often mysterious. An aeon can use this ability to communicate flawlessly with any other aeon on the same plane as itself."
ac: 32
armorclass:
  - name: "AC"
    desc: "32; __Fort__: +23; __Ref__: +22; __Will__: +23 +1 status to all saves vs. [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|magical]]"
hp: 225
health:
  - name: "HP"
    desc: "225; __Immunities__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|vitality]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|void]]; __Weaknesses__ [[srd/pf2e/compendium/rules-elements/traits/player-core/Spirit|spirit]] 10"
abilities_mid:
  - name: "Balance Life"
    desc: "⬲ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|divine]])"
  - name: "Trigger"
    desc: "A creature within 100 feet is about to attempt a [[srd/pf2e/books/player-core/chapter-8-playing-the-game/Hit Points, Healing, and Dying#Recovery Checks|recovery check]]"
  - name: "Effect"
    desc: "The akhana chooses to make the result a success or failure (but not a critical success or failure). This effect gains the [[srd/pf2e/compendium/rules-elements/traits/player-core/Fortune|fortune]] trait if the akhana chooses success or [[srd/pf2e/compendium/rules-elements/traits/player-core/Misfortune|misfortune]] for failure."
speed: "fly 60 feet"
attacks:
  - name: "Melee"
    desc: "⬻ tail +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]]) __Damage__ 5d10 void plus Grab"
  - name: "Melee"
    desc: "⬻ fist +24 ([[srd/pf2e/compendium/rules-elements/traits/player-core/Agile|Agile]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Magical|Magical]]) __Damage__ 3d6+12 bludgeoning plus 1d6 vitality or 1d6 void"
abilities_bot:
  - name: "Flying Fists"
    desc: "⬺ The akhana [[srd/pf2e/compendium/rules-elements/actions/player-core#Fly|Flies]] and makes up to four fist Strikes against different targets at any points during this movement. The attacks count toward its multiple attack penalty normally, but the penalty does not increase until after Flying Fists is complete."
  - name: "Reclaim Life"
    desc: "⬻ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Void|Void]])"
  - name: "Requirements"
    desc: "The akhana has a living creature [[srd/pf2e/compendium/rules-elements/Conditions#Grabbed|grappled]] or [[srd/pf2e/compendium/rules-elements/Conditions#Restrained|restrained]] with its tail"
  - name: "Effect"
    desc: "The creature takes 4d10 void damage with a DC 32 basic Fortitude save. On a failed save, it's also [[srd/pf2e/compendium/rules-elements/Conditions#Doomed|doomed 1]]. If the creature dies while doomed and held in the akhana's tail, its soul is trapped in the akhana (as [[srd/pf2e/compendium/spells/rank-9/Seize Soul|_seize soul_]]), and its remains are preserved as peaceful rest. The soul returns to the body with 1 Hit Point if the akhana Dismisses the effect, if the akhana is slain, or if a [[srd/pf2e/compendium/spells/rituals/Wish|_wish_]] ritual or similarly powerful magic frees it."
  - name: "Sprout Life"
    desc: "⬺ ([[srd/pf2e/compendium/rules-elements/traits/player-core/Concentrate|Concentrate]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Divine|Divine]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Plant|Plant]], [[srd/pf2e/compendium/rules-elements/traits/player-core/Vitality|Vitality]]) A 5-foot burst within 100 feet fills with simple life appropriate to the environment. The newly forged animals bite those in the area for 7d6 piercing damage with a DC 32 basic Reflex save. The akhana can also have fungus or plants choke the area, even floating ones in the sky, creating difficult terrain. The created life lives or dies normally after its creation."
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32 - __Cantrips (6th)__ [[srd/pf2e/compendium/spells/cantrips/Stabilize|Stabilize]], [[srd/pf2e/compendium/spells/cantrips/Vitality Lash|Vitality Lash]], [[srd/pf2e/compendium/spells/cantrips/Void Warp|Void Warp]] - __2nd__ [[srd/pf2e/compendium/spells/rank-2/Peaceful Rest|Peaceful Rest]] (at will) - __4th__ [[srd/pf2e/compendium/spells/rank-1/Harm|Harm]] (at will), [[srd/pf2e/compendium/spells/rank-1/Heal|Heal]] (at will)"
sourcebook: "_Monster Core_, page 10."
```

```encounter-table
name: Akhana
creatures:
  - 1: Akhana
```
