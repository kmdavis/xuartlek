---
obsidianUIMode: preview
noteType: pf2eMonster
aliases: "Lamia Matriarch"
tags:
  - pf2e/creature/level/8
  - pf2e/creature/trait/beast
  - pf2e/creature/trait/humanoid
  - pf2e/creature/trait/large
statblock: inline
name: "Lamia Matriarch"
level: 8
source: "Monster Core"
aon_id: "creature-3078"
aon_url: "https://2e.aonprd.com/Monsters.aspx?ID=3078"
---

```statblock
columns: 2
forcecolumns: true
layout: Basic Pathfinder 2e Layout
source: "MC"
name: "Lamia Matriarch"
level: "Creature 8"
size: "Large"
trait_01: "Beast"
trait_02: "Humanoid"
modifier: 15
perception:
  - name: "Perception"
    desc: "Perception +15; darkvision"
languages: "Chthonian, Common, Draconic"
skills:
  - name: "Skills"
    desc: "Athletics +18, Cult Lore +15, Deception +20, Diplomacy +20, Intimidation +18, Occultism +17, Stealth +16, Survival +13"
abilityMods: [6, 4, 3, 3, 3, 6]
abilities_top:
  - name: "Items"
    desc: "_+1 striking scimitar_"
ac: 27
armorclass:
  - name: "AC"
    desc: "27; __Fort__: +13; __Ref__: +18; __Will__: +17 +1 status to all saves vs. magic"
hp: 135
health:
  - name: "HP"
    desc: "135; __Immunities__ controlled; __Resistances__ mental 10"
speed: "30 feet, climb 30 feet, swim 30 feet"
attacks:
  - name: "Melee"
    desc: "⬻ _scimitar_ +19 (forceful +2, Sweep) __Damage__ 2d6+10 slashing"
abilities_bot:
  - name: "Change Shape"
    desc: "⬻ (Concentrate, Occult, Polymorph) The lamia matriarch can take on the appearance of a Medium humanoid. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it does prevent them from using their cursed touch. Each lamia matriarch has a fixed humanoid form that resembles their upper torso when in their true form. This is the only humanoid form they can adopt using this ability."
  - name: "Matriarch's Caress"
    desc: "⬺ (Curse, Mental, Occult) The lamia touches a creature, who must succeed at a DC 28 Will save or become stupefied 2. If the target fails additional saves against this ability, the condition value increases by 2 (to a maximum of stupefied 4). This condition value decreases by 1 every 24 hours."
  - name: "Scimitar Storm"
    desc: "⬽ The lamia matriarch makes a scimitar attack against each enemy within reach. Each attack counts toward their multiple attack penalty, but the penalty does not increase until after all the attacks. The first enemy they damage is subject to Matriarch's Caress."
spellcasting:
  - name: "Occult Spontaneous Spells"
    desc: "DC 28 - __Cantrips (3rd)__ Daze, Detect Magic, Prestidigitation, Read Aura, Telekinetic Hand - __1st__ Bless, Force Barrage, Phantom Pain, Soothe (4 slots) - __2nd__ Blur, Illusory Creature, Invisibility (4 slots) - __3rd__ Dispel Magic, Enthrall, Haste, Mind Reading (4 slots)"
  - name: "Occult Innate Spells"
    desc: "DC 28 - __1st__ Ventriloquism (at will) - __2nd__ Illusory Disguise (at will), Illusory Object (at will), Blur - __4th__ Charm (×3), Suggestion (×3), Sleep"
sourcebook: "_Monster Core_, page 215."
```

```encounter-table
name: Lamia Matriarch
creatures:
  - 1: Lamia Matriarch
```
