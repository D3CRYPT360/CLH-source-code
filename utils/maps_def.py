import discord
def map_hex(map_name):
    if map_name == "Split":
        return discord.Colour.teal()
    
    elif map_name == "Bind":
        return discord.Colour.dark_gold()
    
    elif map_name == "Haven":
        return discord.Colour.red()
    
    elif map_name == "Ascent":
        return discord.Colour.dark_orange()
    
    elif map_name == "Icebox":
        return discord.Colour.blurple()
    
    elif map_name == "Range":
        return discord.Colour.orange()
    
def lore_link_general(map_name):
    if map_name == "Split":
        return "https://discordapp.com/channels/708983243847761931/747040395891966002/747051202482667602"
    
    elif map_name == "Bind":
        return "https://discord.com/channels/708983243847761931/747040395891966002/747143027440484453"
    
    elif map_name == "Haven":
        return "https://discord.com/channels/708983243847761931/747040395891966002/747392315944992819"
    
    elif map_name == "Ascent":
        return "https://discord.com/channels/708983243847761931/747040395891966002/747136697036177458"
    
    elif map_name == "Icebox":
        return "https://discord.com/channels/708983243847761931/747040395891966002/763054857421848597"
    
    elif map_name == "Range":
        return "https://discord.com/channels/708983243847761931/747040395891966002/748104154362413166"
    
def lore_link_unconfirmed(map_name):
    if map_name == "Split":
        return "https://discordapp.com/channels/708983243847761931/749187232530825266/749326681923256340"
    
    elif map_name == "Bind":
        return "https://discord.com/channels/708983243847761931/749187232530825266/749309432994726011"
    
    elif map_name == "Haven":
        return "https://discord.com/channels/708983243847761931/747040395891966002/747392315944992819"
    
    elif map_name == "Ascent":
        return "https://discord.com/channels/708983243847761931/749187232530825266/749306607669608499"
    
    elif map_name == "Icebox":
        return "https://discord.com/channels/708983243847761931/749187232530825266/763068019030229022"
    
    elif map_name == "Range":
        return "https://discord.com/channels/708983243847761931/747040395891966002/748104154362413166"
    
    
def lore_link_scrapped(map_name):
    if map_name == "Split":
        return "https://discordapp.com/channels/708983243847761931/749305721467699273/749902333302800384"
    
    elif map_name == "Bind":
        return "https://discord.com/channels/708983243847761931/749305721467699273/749898301335142411"
    
    elif map_name == "Haven":
        return "https://discord.com/channels/708983243847761931/749305721467699273/749914184367472713"
    
    elif map_name == "Ascent":
        return "https://discord.com/channels/708983243847761931/749305721467699273/749914435455549480"
    
    elif map_name == "Icebox":
        return "https://discord.com/channels/708983243847761931/749305721467699273/763323710764613632"
    
    elif map_name == "Range":
        return "https://discord.com/channels/708983243847761931/749305721467699273/765456380576137234"
    
def maps_codename(map_name):
    if map_name == "Split":
        return "Bonsai"
    
    elif map_name == "Bind":
        return "Duality"
    
    elif map_name == "Haven":
        return "Triad"
    
    elif map_name == "Ascent":
        return "Venice"
    
    elif map_name == "Icebox":
        return "Port"
    
    elif map_name == "Range":
        return "Poveglia"
    
def maps_real(map_name):
    if map_name == "Split":
        return "Tokyo/Japan"
    
    elif map_name == "Bind":
        return "Rabat/Morroco"
    
    elif map_name == "Haven":
        return "Thimphu/Bhutan"
    
    elif map_name == "Ascent":
        return "Venice/Italy"
    
    elif map_name == "Icebox":
        return "Bennett Island/Russia"
    
    elif map_name == "Range":
        return "Venice/Italy"