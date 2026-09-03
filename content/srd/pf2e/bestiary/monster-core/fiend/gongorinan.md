---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Gongorinan"
tags:
  - pf2e/creature/level/11
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/qlippoth
  - pf2e/creature/trait/uncommon
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/medium
statblock: inline
name: "Gongorinan"
level: 11
source: "Monster Core"
aon_id: "creature-3155"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3155"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Gongorinan"
level: "Creature 11"
size: "Medium"
trait_01: "Fiend"
trait_02: "Qlippoth"
trait_03: "Uncommon"
trait_04: "Unholy"
modifier: 20
perception:
  - name: "Perception"
    desc: "Perception +20; darkvision"
languages: "Chthonian; telepathy 100 feet"
skills:
  - name: "Skills"
    desc: "Acrobatics +23, Athletics +23, Intimidation +21, Stealth +21"
abilityMods: [6, 6, 7, 1, 3, 4]
abilities_top:
  - name: "Items"
    desc: "_+1 striking club_"
ac: 31
armorclass:
  - name: "AC"
    desc: "31; __Fort__: +24; __Ref__: +21; __Will__: +20"
hp: 205
health:
  - name: "HP"
    desc: "205; __Immunities__ controlled, fear; __Resistances__ mental 10, physical 10 (except cold iron)"
speed: "40 feet, climb 40 feet, fly 40 feet; unfettered movement"
attacks:
  - name: "Melee"
    desc: "⬻ club +24 __Damage__ 2d6+9 bludgeoning plus reject tools"
  - name: "Melee"
    desc: "⬻ pincer +23 (Magical, Unholy) __Damage__ 2d10+9 slashing plus 2d6 mental and Grab"
  - name: "Melee"
    desc: "⬻ tentacle +23 (Agile, Magical, reach 10 feet, Unholy) __Damage__ 2d6+9 bludgeoning plus 2d6 mental"
  - name: "Melee"
    desc: "⬻ stinger +23 (Magical, Unholy) __Damage__ 2d6+9 piercing plus gongorinan venom"
abilities_bot:
  - name: "Disquieting Display"
    desc: "⬺ (Concentrate, Mental, Occult, Visual) The gongorinan opens its maw to reveal the forms hidden there, making observers question their own bodies. Creatures in a 30-foot emanation must attempt a DC 30 Will save, after which they are temporarily immune to further Disquieting Displays for 1 minute."
  - name: "Critical Success"
    desc: "The creature is unaffected."
  - name: "Success"
    desc: "The creature is clumsy 1 for 1 round."
  - name: "Failure"
    desc: "The creature is clumsy 2 and slowed 1 for 1 round."
  - name: "Critical Failure"
    desc: "As failure, but for 1 minute."
  - name: "Gongorinan Venom"
    desc: "(Poison, Polymorph)"
  - name: "Saving Throw"
    desc: "Fortitude DC 30"
  - name: "Stage 1"
    desc: "stupefied 1 and cosmetic signs appear of turning into an animal, fungus, or plant (1 round)"
  - name: "Stage 2"
    desc: "stupefied 2 and clumsy 2 (1 round)"
  - name: "Stage 3"
    desc: "stupefied 4 and clumsy 4 (1 round)"
  - name: "Stage 4"
    desc: "paralyzed as changes completely overtake the body (1 round)"
  - name: "Stage 5"
    desc: "the victim permanently transforms into an animal, fungus, or plant in mind and body as a permanent curse, and the affliction ends"
  - name: "Painful Limbs"
    desc: "⬺ The gongorinan makes up to four Strikes against different targets, each using a different limb. All four Strikes count toward its multiple attack penalty, but the penalty doesn't increase until after the gongorinan has made all the attacks."
  - name: "Reject Tools"
    desc: "(Mental, Occult) A creature hit by the gongorinan's club must succeed at a DC 30 Will save or Release any manufactured items it's holding."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 30 - __3rd__ One with Stone (at will) - __6th__ Cursed Metamorphosis, Petrify - __Constant (4th)__ Unfettered Movement"
sourcebook: "_Monster Core_, page 281."
```

```encounter-table
name: Gongorinan
creatures:
  - 1: Gongorinan
```
