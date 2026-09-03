---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Evangelist"
tags:
  - pf2e/creature/level/6
  - pf2e/creature/trait/fiend
  - pf2e/creature/trait/unholy
  - pf2e/creature/trait/velstrac
  - pf2e/creature/trait/medium
statblock: inline
name: "Evangelist"
level: 6
source: "Monster Core 2"
aon_id: "creature-4608"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4608"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Evangelist"
level: "Creature 6"
size: "Medium"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: "Velstrac"
modifier: 13
perception:
  - name: "Perception"
    desc: "Perception +13; greater darkvision, painsight"
languages: "Common, Diabolic, Shadowtongue"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +15, Crafting +10, Intimidation +15, Religion +11, Torture Lore +12"
abilityMods: [4, 3, 2, 0, 1, 1]
abilities_top:
  - name: "Painsight"
    desc: "(divine) A velstrac automatically knows whether a creature it sees has any of the doomed, dying, and wounded conditions as well as the value of those conditions."
ac: 24
armorclass:
  - name: "AC"
    desc: "24; __Fort__: +15; __Ref__: +14; __Will__: +11 +1 status to all saves vs. magic"
hp: 90
health:
  - name: "HP"
    desc: "90 , regeneration 10 (deactivated by holy or silver); __Immunities__ cold; __Weaknesses__ holy 5, silver 5"
abilities_mid:
  - name: "Unnerving Gaze"
    desc: "(aura, divine, fear, mental, visual) 30 feet. When a creature ends its turn in the aura, it sees the face of a departed loved one in place of the evangelist's face. The creature must succeed at a DC 21 Will save or become frightened 2 (frightened 3 on a critical failure)."
  - name: "Reactive Strike"
    desc: "⬲"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _morningstar_ +17 (Magical, unholy, versatile P) __Damage__ 2d6+7 bludgeoning plus 1d6 persistent bleed and grievous wound"
abilities_bot:
  - name: "Focus Gaze"
    desc: "⬻ (Concentrate, divine, fear, mental, visual) The evangelist stares at a creature they can see within 30 feet. The target must immediately attempt a Will save against unnerving gaze. In addition, if the creature was already frightened, on a failed save, the evangelist is concealed from the creature for as long as the creature remains frightened. After attempting this save, the creature is then temporarily immune to Focus Gaze until the start of the evangelist's next turn."
  - name: "Grievous Wound"
    desc: "When the evangelist critically hits with a morningstar Strike, the target's wound is particularly gruesome and disorienting. The creature becomes clumsy 1, and the DC to recover from its persistent bleed damage is 17 (DC 12 when receiving especially appropriate assistance). The clumsy condition doesn't end until the creature recovers from its persistent bleed."
  - name: "Unleash Weapon"
    desc: "⬺ The evangelist releases their morningstar and commands the augur trapped within to attack. The weapon flies off and the evangelist makes up to two morningstar Strikes, each against a different target within 20 feet. These attacks count against the evangelist's multiple attack penalty, but the multiple attack penalty doesn't increase until after all the attacks. The morningstar then returns to the evangelist's hand."
sourcebook: "_Monster Core 2_, page 346."
```

```encounter-table
name: Evangelist
creatures:
  - 1: Evangelist
```
