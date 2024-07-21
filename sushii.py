import discord


basic_roles_list = [673276401037606961,668556934252593152,683406500412260374,748601760813416528]
anniv_roles_list = [860659579061796874, 860659766341664798, 860659805684236298, 860660150688022538, 860660179904626699, 860659627670634496, 860659677992976394, 860659882437246986, 860659914643996672, 860660111809576990, 860659454080057375, 860659532992741406, 860659838761959446, 860659953777508413, 860660067904520214]


class BasicRolesButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Updates',custom_id="bsrbutton-1",style=discord.ButtonStyle.grey,emoji=":KAC:")
    async def but1(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(basic_roles_list[0])
        await bsrfn(interaction,discord.Client.role)

    @discord.ui.button(label='Games',custom_id="bsrbutton-2",style=discord.ButtonStyle.grey,emoji=":video_game:")
    async def but2(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(basic_roles_list[1])
        await bsrfn(interaction,discord.Client.role)

    @discord.ui.button(label='Waifu',custom_id="bsrbutton-3",style=discord.ButtonStyle.grey,emoji=":two_hearts:")
    async def but3(self,interaction:discord.Interaction, Button:discord.ui.button):
        discord.Client.role=interaction.guild.get_role(basic_roles_list[2])
        await bsrfn(interaction,discord.Client.role)

    @discord.ui.button(label='Paimon',custom_id="bsrbutton-4",style=discord.ButtonStyle.grey,emoji=":1Hulalalala:")
    async def but4(self,interaction:discord.Interaction, Button:discord.ui.button):
        discord.Client.role=interaction.guild.get_role(basic_roles_list[3])
        await bsrfn(interaction,discord.Client.role)

async def bsrfn(interaction,role):
    for x in range(len(basic_roles_list)):
        temp_role = interaction.guild.get_role(basic_roles_list[x])
        if temp_role in interaction.user.roles:
            await interaction.user.remove_roles(temp_role)
            break
    await interaction.user.add_roles(role)
    await interaction.response.send_message(f"Currently selected role : {role.mention}", ephemeral=True, delete_after=5)


class AnnivRolesButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=None,custom_id="annivbutton-1",row=0,style=discord.ButtonStyle.grey,emoji="<:WindborneBard:1263891213036294174>")
    async def annivbut1(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[0])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-2",row=0,style=discord.ButtonStyle.grey,emoji="<:VigilantYaksha:1263891204718858251>")
    async def annivbut2(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[1])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-3",row=0,style=discord.ButtonStyle.grey,emoji="<:SpindriftKnight:1263891150029459498>")
    async def annivbut3(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[2])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-4",row=1,style=discord.ButtonStyle.grey,emoji="<:HerMajestyTsaritsa:1263891056420847758>")
    async def annivbut4(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[3])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-5",row=1,style=discord.ButtonStyle.grey,emoji="<:CinderOfTwoWorldsFlames:1263890908781219881>")
    async def annivbut5(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[4])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-6",row=1,style=discord.ButtonStyle.grey,emoji="<:DeusAuri:1263890929459400852>")
    async def annivbut6(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[5])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-7",row=2,style=discord.ButtonStyle.grey,emoji="<:NarukamiOgosho:1263891101140389899>")
    async def annivbut7(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[6])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-8",row=2,style=discord.ButtonStyle.grey,emoji="<:LadyOfFire:1263891072220790856>")
    async def annivbut8(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[7])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-9",row=2,style=discord.ButtonStyle.grey,emoji="<:ShoukiNoKami:1263891121562452019>")
    async def annivbut9(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[8])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-10",row=3,style=discord.ButtonStyle.grey,emoji="<:ValleyOrchid:1263891192668618805>")
    async def annivbut10(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[9])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-11",row=3,style=discord.ButtonStyle.grey,emoji="<:HelmOfTheRadiantRose:1263890947582722079>")
    async def annivbut11(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[10])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-12",row=3,style=discord.ButtonStyle.grey,emoji="<:QueenAranyani:1263891110267191297>")
    async def annivbut12(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[11])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-13",row=4,style=discord.ButtonStyle.grey,emoji="<:UsurperOfManyWaters:1263891168790581279>")
    async def annivbut13(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[12])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-14",row=4,style=discord.ButtonStyle.grey,emoji="<:DevourerOfDivinity:1263890938372030708>")
    async def annivbut14(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[13])
        await anrfn(interaction,discord.Client.role)

    @discord.ui.button(label=None,custom_id="annivbutton-15",row=4,style=discord.ButtonStyle.grey,emoji="<:TwilightSword:1263891159269376043>")
    async def annivbut15(self,interaction:discord.Interaction, Button: discord.ui.button):
        discord.Client.role=interaction.guild.get_role(anniv_roles_list[14])
        await anrfn(interaction,discord.Client.role)

async def anrfn(interaction,role):
    for x in range(len(anniv_roles_list)):
        temp_role = interaction.guild.get_role(anniv_roles_list[x])
        if temp_role in interaction.user.roles:
            await interaction.user.remove_roles(temp_role)
            break
    await interaction.user.add_roles(role)
    await interaction.response.send_message(f"Currently selected role : {role.mention}", ephemeral=True, delete_after=5)


class RmAnnivButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=None,custom_id="rmanniv",style=discord.ButtonStyle.grey,emoji="<:None:1262992717315571744>")
    async def rmannivbut(self,interaction:discord.Interaction, Button:discord.ui.Button):
        for x in range(len(anniv_roles_list)):
            temp_role = interaction.guild.get_role(anniv_roles_list[x])
            if temp_role in interaction.user.roles:
                await interaction.user.remove_roles(temp_role)
                await interaction.response.send_message(f"{temp_role.mention} has been removed from you",ephemeral=True, delete_after=5)
                break



