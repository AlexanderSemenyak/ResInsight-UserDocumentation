+++
title = "Windows Installation"
published = true
hidden = false
weight = 20
+++

### ResInsight Installation

1. Download ZIP binary distribution from [https://github.com/OPM/ResInsight/releases](https://github.com/OPM/ResInsight/releases "release section on GitHub")
2. Extract content from ZIP file
3. Start ResInsight.exe 

{{% notice info %}}
The binary distribution does not support ABAQUS odb files. For building ResInsight with ABAQUS support, see 
[Build Instructions]({{< ref "buildinstructions.md" >}}).
{{% /notice %}}


### Octave Installation (optional)
1. Download [Octave-4.0.0](ftp://ftp.gnu.org/gnu/octave/windows) and install it. (Newer versions will not work)
2. Launch ResInsight.exe, open **Edit->Preferences**. 
3. On the **Octave** tab, enter the path to the Octave command line interpreter executable.  
   ( Usually _`C:\Your\Path\To\Octave-x.x.x\bin\octave-cli.exe`_ )

{{% notice info %}}
A binary package of ResInsight will normally <b>not</b> work with other Octave versions than the one it is compiled with. 
{{% /notice %}}

{{% notice info %}}
You <b>have</b> to point to the <b>cli</b> binary in the windows octave installation. The <code>octave.exe</code> will not work as it is launching the octave GUI.
{{% /notice %}}
