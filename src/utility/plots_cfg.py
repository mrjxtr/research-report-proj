"""
Module for configuring plot aesthetics using Matplotlib and Seaborn.

This module provides functions to set a custom color palette and apply
consistent theming across plots created with Matplotlib and Seaborn.
"""

import matplotlib as mpl
import seaborn as sns
from cycler import cycler


def set_custom_palette():
    """
    Define and return a custom color palette.

    Returns:
        dict: A dictionary containing custom color values for different levels.
    """
    return {
        "high": "#1f77b4",  # Deep blue for high/important values
        "high-mid": "#6baed6",  # Sky blue for values slightly below high
        "mid": "#9ecae1",  # Light blue for moderate values
        "low-mid": "#c6dbef",  # Very light blue for values slightly above low
        "low": "#f0f0f0",  # Very light grey for low/least important values
    }


def apply_theme(custom_palette):
    """
    Apply Seaborn and Matplotlib theme with the custom palette.

    Args:
        custom_palette (dict): A dictionary containing custom color values for different levels.
    """
    palette_list = [
        custom_palette["high"],  # Deep blue
        custom_palette["high-mid"],  # Sky blue
        custom_palette["mid"],  # Light blue
        custom_palette["low-mid"],  # Very light blue
        custom_palette["low"],  # Very light grey
    ]

    # Apply Seaborn theme
    sns.set_theme(style="whitegrid", palette=palette_list)

    # Update Matplotlib settings
    mpl.rcParams.update(
        {
            "figure.figsize": (16, 9),  # Set default figure size
            "axes.facecolor": "white",  # Set axes background color
            "axes.grid": True,  # Enable grid lines
            "grid.color": "lightgray",  # Set grid line color
            "axes.prop_cycle": cycler(color=palette_list),  # Apply custom color cycle
            "axes.linewidth": 1,  # Set axes line width
            "xtick.color": "black",  # Set x-axis tick label color
            "ytick.color": "black",  # Set y-axis tick label color
            "font.size": 12,  # Set default font size
            "figure.titlesize": 24,  # Set figure title font size
            "figure.dpi": 100,  # Set figure resolution
            "axes.labelcolor": "black",  # Set axes label color
            "font.family": "sans-serif",  # Set default font family
            "font.sans-serif": [
                "Arial",
                "DejaVu Sans",
                "Liberation Sans",
            ],  # Specify sans-serif fonts
            "text.color": "black",  # Set default text color
            "axes.titlecolor": "black",  # Set axes title color
            "axes.titlesize": 14,  # Set axes title font size
            "axes.labelsize": 12,  # Set axes label font size
            "xtick.labelsize": 10,  # Set x-axis tick label font size
            "ytick.labelsize": 10,  # Set y-axis tick label font size
            "legend.fontsize": 10,  # Set legend font size
            "legend.loc": "best",  # Set legend location
            "lines.linewidth": 1.5,  # Set line width
            "patch.edgecolor": "black",  # Set patch edge color
            "patch.force_edgecolor": True,  # Force patch edge color
            "image.cmap": "Blues",  # Set default colormap for images
            "savefig.dpi": 300,  # Set resolution of saved figures
            "savefig.facecolor": "white",  # Set background color of saved figures
            "savefig.edgecolor": "white",  # Set edge color of saved figures
            "savefig.format": "png",  # Set default format for saving figures
            "axes.spines.top": False,  # Hide top spine
            "axes.spines.right": False,  # Hide right spine
            "axes.spines.left": True,  # Show left spine
            "axes.spines.bottom": True,  # Show bottom spine
            "axes.edgecolor": "black",  # Set axes edge color
            "axes.grid.axis": "y",  # Show grid lines on y-axis
            "axes.grid.which": "both",  # Show both major and minor grid lines
            "grid.linestyle": "--",  # Set grid line style
            "grid.linewidth": 0.5,  # Set grid line width
            "xtick.major.size": 5,  # Set major tick size on x-axis
            "xtick.minor.size": 3,  # Set minor tick size on x-axis
            "ytick.major.size": 5,  # Set major tick size on y-axis
            "ytick.minor.size": 3,  # Set minor tick size on y-axis
            "xtick.major.width": 1,  # Set major tick width on x-axis
            "xtick.minor.width": 0.5,  # Set minor tick width on x-axis
            "ytick.major.width": 1,  # Set major tick width on y-axis
            "ytick.minor.width": 0.5,  # Set minor tick width on y-axis
            "xtick.direction": "out",  # Set x-axis ticks to point outwards
            "ytick.direction": "out",  # Set y-axis ticks to point outwards
            "legend.frameon": True,  # Draw frame around legend
            "legend.framealpha": 0.8,  # Set legend frame transparency
            "legend.fancybox": True,  # Use rounded box for legend frame
            "legend.shadow": False,  # Do not add shadow to legend
            "legend.borderaxespad": 0.5,  # Set padding between legend and axes
            "legend.borderpad": 0.5,  # Set padding inside legend box
            "legend.columnspacing": 1.0,  # Set spacing between columns in legend
            "legend.handletextpad": 0.5,  # Set padding between legend handle and text
            "legend.handlelength": 2.0,  # Set length of legend handles
            "legend.labelspacing": 0.5,  # Set vertical space between legend entries
        }
    )


def load_cfg():
    """
    Load all Matplotlib and Seaborn settings into the caller's namespace.

    This function sets the custom color palette and applies the theme settings
    for Matplotlib and Seaborn.
    """
    custom_palette = set_custom_palette()  # Define the custom color palette
    apply_theme(custom_palette)  # Apply the custom theme settings
