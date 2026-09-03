---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Redcap"
tags:
  - pf2e/creature/level/5
  - pf2e/creature/trait/fey
  - pf2e/creature/trait/small
statblock: inline
name: "Redcap"
level: 5
source: "Monster Core"
aon_id: "creature-3165"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3165"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Redcap"
level: "Creature 5"
size: "Small"
trait_01: "Fey"
modifier: 12
perception:
  - name: "Perception"
    desc: "Perception +12; low-light vision"
languages: "Common, Fey"
skills:
  - name: "Skills"
    desc: "Acrobatics +13, Athletics +15, Deception +11, Intimidation +13, Nature +10, Stealth +13"
abilityMods: [4, 4, 2, 1, 1, 2]
abilities_top:
  - name: "Red Cap"
    desc: "(primal) A redcap's woolen hat is dyed with the blood of their victims. If the redcap loses their cap, they no longer benefit from fast healing and take a –4 status penalty to their damage rolls. They can create a new cap in 10 minutes, but that cap doesn't grant them powers until the redcap has turned it red with Blood Soak. A cap has no benefit for creatures other than the redcap who made it."
  - name: "Items"
    desc: "Halberd, iron boots, red cap"
ac: 21
armorclass:
  - name: "AC"
    desc: "21; __Fort__: +11; __Ref__: +15; __Will__: +10"
hp: 60
health:
  - name: "HP"
    desc: "60 (fast healing 10); __Weaknesses__ cold iron 5, divine revulsion"
abilities_mid:
  - name: "Divine Revulsion"
    desc: "(emotion, fear, mental) If a redcap sees a creature brandish a religious symbol of a deity (which requires an Interact action by that creature) or cast a divine spell while wearing a religious symbol, the redcap must attempt a DC 19 Will save. They then become temporarily immune to all brandished religious symbols for 10 minutes."
  - name: "Critical Success"
    desc: "The redcap is unaffected."
  - name: "Success"
    desc: "The redcap is frightened 2."
  - name: "Failure"
    desc: "The redcap gains the fleeing condition for 1 round and is frightened 4."
speed: "50 feet"
attacks:
  - name: "Melee"
    desc: "⬻ halberd +15 (reach 10 feet, versatile S) __Damage__ 1d10+10 slashing"
  - name: "Melee"
    desc: "⬻ iron boot +13 (Agile, versatile B) __Damage__ 1d6+8 piercing"
abilities_bot:
  - name: "Blood Soak"
    desc: "⬻ (Manipulate) The redcap dips their cap in the blood of a slain foe. The foe must have died in the last minute, and the redcap must have helped kill it. The redcap gains a +4 status bonus to damage rolls for 1 minute."
  - name: "Deadly Cleave"
    desc: "⬲"
  - name: "Trigger"
    desc: "The redcap reduces a creature to 0 Hit Points with a halberd Strike"
  - name: "Effect"
    desc: "The redcap makes another halberd Strike against a different creature, using the same multiple attack penalty as the halberd Strike that triggered this reaction. This counts toward their multiple attack penalty as normal."
  - name: "Stomp"
    desc: "⬻ The redcap Strides up to half their Speed and makes a boot Strike at any point during that movement. If the boot Strike hits a prone creature, it deals an extra 2d6 persistent bleed damage. Stomping Ground Unlike some fey, redcaps don't embody a particular natural feature or environment, so they can be found almost anywhere. They tend to prefer areas that allow them to hide or at least get behind cover with their quick movement, such as forests, mountains, and underground tunnels and caverns. Sometimes they take up residence in abandoned buildings, especially barns and sheds."
sourcebook: "_Monster Core_, page 290."
```

```encounter-table
name: Redcap
creatures:
  - 1: Redcap
```
