import streamlit as st


def style_background_team_fdr(cell_value):
    """Used to apply background highlighting to the teams FDR matrix"""

    bg = "background-color:"
    team_str = 0

    if cell_value != "":
        team_str = int(cell_value[-1])

    if team_str == 1:
        return f"{bg} darkgreen;"
    elif team_str == 2:
        return f"{bg} #09fc7b;"
    elif team_str == 3:
        return f"{bg} #e7e7e8;"
    elif team_str == 4:
        return f"{bg} #ff1651; color: #ffffff;"
    elif team_str == 5:
        return f"{bg} #80072d; color: #ffffff;"
    else:
        return ""


def style_background_player_fdr(cell_value):
    """Used to apply background highlighting to the player FDR matrix"""

    bg = "background-color:"

    if cell_value == 1:
        return f"{bg} darkgreen;"
    elif cell_value == 2:
        return f"{bg} #09fc7b;"
    elif cell_value == 3:
        return f"{bg} #e7e7e8;"
    elif cell_value == 4:
        return f"{bg} #ff1651; color: #ffffff;"
    elif cell_value == 5:
        return f"{bg} #80072d; color: #ffffff;"
    else:
        return ""


style_players = {
    "pos": st.column_config.TextColumn("Pos", help="Position"),
    "player_name": st.column_config.TextColumn("Player"),
    "team": st.column_config.TextColumn("Team"),
    "£": st.column_config.NumberColumn("£", help="Current price"),
    "ST": st.column_config.NumberColumn("ST", help="Games started"),
    "MP": st.column_config.NumberColumn("MP", help="Minutes played"),
    "Pts": st.column_config.NumberColumn("Pts", help="Points scored"),
    "Pts90": st.column_config.NumberColumn("P90", help="Points / 90 minutes"),
    "GS90": st.column_config.NumberColumn("GS90", help="Goals / 90 minutes"),
    "A90": st.column_config.NumberColumn("A90", help="Assists / 90 minutes"),
    "GI90": st.column_config.NumberColumn("GI90", help="(G + A) / 90 minutes"),
    "xG90": st.column_config.NumberColumn("xG90", help="Expected goals / 90 minutes"),
    "xA90": st.column_config.NumberColumn("xA90", help="Expected assists / 90 minutes"),
    "xGI90": st.column_config.NumberColumn("xGI90", help="(xG + xA) / 90 minutes"),
    "CS": st.column_config.NumberColumn("CS", help="Clean sheets"),
    "xGC": st.column_config.NumberColumn("xGC", help="Expected goals conceded"),
    "xGC90": st.column_config.NumberColumn("xGC90", help="xG conceded / 90 minutes"),
    "TSB%": st.column_config.NumberColumn("TSB%", help="Teams selected by %"),
}
