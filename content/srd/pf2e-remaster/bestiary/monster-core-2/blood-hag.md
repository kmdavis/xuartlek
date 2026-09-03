---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Blood Hag"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/hag
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/medium
statblock: inline
name: "Blood Hag"
level: 8
source: "Monster Core 2"
aon_id: "creature-4435"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=4435"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC2"
name: "Blood Hag"
level: "Creature 8"
size: "Medium"
trait_01: "Hag"
trait_02: "Humanoid"
modifier: 17
perception:
  - name: "Perception"
    desc: "Perception +17; bloodsense (imprecise) 90 feet, darkvision"
languages: "Aklo, Chthonian, Common, Diabolic, Jotun"
skills:
  - name: "Skills"
    desc: "Acrobatics +15, Athletics +18, Deception +19, Diplomacy +17, Occultism +16, Stealth +17"
abilityMods: [4, 5, 2, 2, 3, 5]
abilities_top:
  - name: "Bloodsense"
    desc: "A blood hag can sense the presence of blood and creatures with blood. They can tell the difference between spilled blood and the blood within a living creature."
  - name: "Coven"
    desc: "A blood hag adds _aerial form_, _fiery body_, and _nightmare_ to their coven's spells."
  - name: "Borrowed Skin"
    desc: "A blood hag wears a covering of skin stolen from a humanoid creature they've killed, hiding their true form. They appear as the creature whose skin they're wearing, including to spells that would detect that creature. Creatures can still potentially detect the deception as described in the Impersonate action. Spreading coarse salt inside the skin prevents the hag from putting it back on, forcing them to keep their fiery form until they kill another humanoid and spend 1 hour turning it into a new disguise."
ac: 26
armorclass:
  - name: "AC"
    desc: "26; __Fort__: +14; __Ref__: +17; __Will__: +17"
hp: 155
health:
  - name: "HP"
    desc: "155; __Immunities__ bleed; __Resistances__ fire 10; __Weaknesses__ cold iron 10"
speed: "25 feet"
attacks:
  - name: "Melee"
    desc: "⬻ jaws +18 __Damage__ 2d12+7 piercing"
  - name: "Melee"
    desc: "⬻ claw +18 (Agile) __Damage__ 2d8+7 slashing plus Grab"
  - name: "Ranged"
    desc: "⬻ firebolt +19 (Agile, fire, occult, range 60 feet) __Damage__ 5d6 fire"
abilities_bot:
  - name: "Assume Fiery Form"
    desc: "⬽ (Concentrate, fire, occult, polymorph) The blood hag removes their borrowed skin and transforms into a brilliant ball of fire. They become amorphous (allowing them to move through a gap at least 1 foot wide without Squeezing and move at full Speed while Squeezing), gain the fire trait and a fly Speed of 60 feet, become immune to fire, and emit light as a torch. They lose their melee Strikes and can't Drain Blood, but they deal 4d6 fire damage with a DC 26 basic Reflex save to each creature that touches them, including a creature that hits them with an unarmed attack or a weapon attack from an adjacent space. If their skin is intact and they're adjacent to it, they can Interact to return to their normal form inside the skin. The hag can choose to Assume Fiery Form as a single action, bursting through their skin in a blast of flames. Doing so destroys their borrowed skin and deals 9d6 fire damage to all creatures in a 20-foot emanation with a DC 26 basic Reflex save."
  - name: "Drain Blood"
    desc: "⬻ (Occult)"
  - name: "Requirements"
    desc: "A grabbed, paralyzed, restrained, unconscious, or willing creature is within the blood hag's reach"
  - name: "Effect"
    desc: "The hag sinks their fangs into the creature to drink its blood. This requires a successful Athletics check against the victim's Fortitude DC if the victim is grabbed and is automatic for any of the other conditions. The victim becomes drained 1. The hag regains 15 Hit Points, gaining any excess HP as temporary Hit Points that last for 1 hour. Drinking blood from a creature that's already drained doesn't restore any Hit Points to the hag but increases the victim's drained value by 1, killing the victim when it reaches drained 5. A victim's drained condition decreases by 1 per week. A blood transfusion, which requires a successful DC 20 Medicine check and sufficient blood or a blood donor, reduces the drained condition by 1 after 10 minutes. Blood Hag Skin A slain blood hag's skin can be used as a component in dark rituals invoking demonic powers. A hero who knows this usually destroys the skin. Less scrupulous adventurers can sell this prize for a substantial sum (80–120 gp). They might later learn that they've helped the buyer unleash a terrible scourge upon the world—if the buyer doesn't kill them first."
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 26 - __4th__ Charm, Sleep (×3)"
sourcebook: "_Monster Core 2_, page 188."
```

```encounter-table
name: Blood Hag
creatures:
  - 1: Blood Hag
```
