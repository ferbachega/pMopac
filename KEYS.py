MOPAC_KEYS = '''
&                     = Turn next line into keywords
+                     = Add another line of keywords
++                    = Split a line of keywords
0SCF                  = Read in data, then stop
1ELECTRON             = Print final one-electron matrix
1SCF                  = Do one scf and then stop
ADD-H 	              = Add hydrogen atoms (intended for use with organic compounds)
A0 	                  = Input geometry is in atomic units
AIDER                 = Read in ab-initio derivatives
AIGIN                 = Geometry must be in Gaussian format
AIGOUT                = Print the geometry in Gaussian format in the ARC file
ALLBONDS 	          = Print final bond-order matrix, including bonds to hydrogen
ALLVEC                = Print all vectors
ALT_A=A 	          = In PDB files with alternative atoms, select atoms A
ALT_R=A 	          = Deleted. All inserted residues are automatically recognized
ANGSTROMS 	          = Input geometry is in Angstroms
AUTOSYM               = Symmetry to be imposed automatically
AUX 	              = Output auxiliary information for use by other programs
AM1                   = Use the AM1 hamiltonian
BANANA  	          = Generate localized molecular orbitals with hybrid orbitals for double bonds
BAR=n.nn              = reduce bar length by a maximum of n.nn%
BCC                   = (Unique)Only even unit cells used (used by BZ)
BIGCYCLES=n           = Do a maximum of n big steps
BIRADICAL             = System has two unpaired electrons
BFGS         	      = Use the Flepo or BFGS geometry optimizer
BONDS                 = Print final bond-order matrix
CAMP                  = Use Camp-King converger in SCF
CARTAB                = Print point-group character table
C.I.=n                = A multi-electron configuration interaction specified
C.I.=(n,m)            = A multi-electron configuration interaction specified
CHAINS(text) 	      = In a protein, explicitely define the letters of chains.
CHECK 	              = Report possible faults in input geometry
CHARGE=n              = Charge on system = n (e.g. NH4 = +1)
CHARGES               = Print net charge on system, and all charges in the system
CHARST                = Print details of working in CHARST
CIS                   = C.I. uses 1 electron excitations only
CISD                  = C.I. uses 1 and electron excitations
CISDT                 = C.I. uses 1, 2 and 3 electron excitations
COMPARE               = Compare the geometries of two systems
COMPFG                = Print heat of formation calculated in COMPFG
COSCCH 	              = Add in COSMO charge corrections
COSWRT                = Write details of the solvent accessible surface to a file
CUTOFP=n.nn           = Madelung distance cutoff is n.nn Angstroms. This can speed up the calculations
CUTOFF=n.nn 	      = In MOZYME, the interatomic distance where the NDDO approximation stops
CUTOFS=n.nn 	      = In MOZYME, the interatomic distance beyond which overlap integrals are ignored
CYCLES=n              = Do a maximum of n steps
CVB         	      = In MOZYME. add and remove specific bonds to allow a Lewis or PDB structure.
DAMP=n.nn 	          = n MOZYME. damp SCF oscillations using a factor of n.nn
DATA=text    	      = Input data set is re-defined to text
DCART                 = Print part of working in DCART
DDMAX=n.nn            = See EF code
DDMIN=n.nn            = Minimum trust radius in a EF/TS calculation
DEBUG                 = Debug option turned on
DEBUG PULAY           = Print working in PULAY
DENOUT, DENOUTF       = Density matrix output
DENSITY               = Print final density matrix
DERI1                 = Print part of working in DERI1
DERI2                 = Print part of working in DERI2
DERITR                = Print part of working in DERIT
DERIV                 = Print part of working in DERIV
DERNVO                = Print part of working in DERNVO
DFORCE                = Force calculation specified, also print force matrix.
DFP                   = Use Davidson-Fletcher-Powell method to optimize geometries
DIPOLE                = In animations graphs, replace ΔHf with dipole
DISEX=n.nn            = Distance for interactions in fine grid in COSMO
DISP 	              = Print the hydrogen bonding and dispersion contributions to the heat of formation
DMAX=n.nn             = Maximum stepsize in eigenvector following
DOUBLET               = Doublet state required
DRC                   = Dynamic reaction coordinate calculation
DRC=n.nnn             = Dynamic reaction coordinate calculation
DUMP=nn.nn            = Write restart files every n seconds
ECHO                  = Data are echoed back before calculation starts
EF                    = Use the EigenFollowing routine for geometry optimization
EIGEN 	              = Print canonical eigenvectors instead of LMOs in MOZYME calculations
EIGS                  = Print all eigenvalues in ITER
ENPART                = Partition energy into components
EPS=n.nn              = Dielectric constant in COSMO calculation
ESP                   = Do not use.  Use GRAPHF instead.
ESPGRID=n 	          = Do not use.  Use GRAPHF instead.
ESR                   = Calculate RHF spin density
EXCITED               = Optimize first excited singlet state
EXTERNAL=name         = Read parameters off disk
FIELD=(n.nn,m.mm,l.ll)= An external electric field is to be used
FILL=n                = In RHF open and closed shell, force M.O. n to be filled
FLEPO                 = Print details of geometry optimization
FMAT                  = Print details of working in FMAT
FOCK                  = Print last Fock matrix
FREQCY                = Print symmetrized Hessian in a FORCE calculation
FORCE, FORCETS        = Calculate vibrational frequencies
GEO-OK                = Override some safety checks
GEO_DAT=<text> 	      = Read in geometry from the file <text>
GEO_REF=<text> 	      = Read in a second geometry from the file <text>
GNORM=n.nn            = Exit when gradient norm drops below n .n kcal/mol/Angstrom
GRADIENTS             = Print all gradients
GRAPH                 = Generate unformatted file for graphics
GRAPHF                = Generate formatted file for graphics suitable for  Jmol and MOPETE.
HCORE 	              = Print all parameters used, the one-electron matrix, and two-electron integrals
HESSIAN 	          = Print Hessian from geometry optimization
HESS=n                = Options for calculating Hessian matrices in EF
H-PRIORITY            = heat of formation takes priority in DRC
H-PRIORITY=n.nn       =  
HYPERFINE             = Hyperfine coupling constants to be calculated
INT                   = Make all coordinates internal coordinates
INVERT 	              = Reverse all optimization flags
IONIZE 	              = Do not use - use SITE=(IONIZE) instead
IRC                   = Intrinsic reaction coordinate calculation
IRC=n                 = 
ISOTOPE               = Force matrix written to disk (channel 9 )
ITER                  = Print details of working in ITER
ITRY=nn               = Set limit of number of SCF iterations to n
IUPD=n                = Mode of Hessian update in eigenvector following
KINETIC=n.nnn         = Excess kinetic energy added to DRC calculation
KING                  = Use Camp-King converger for SCF
LARGE                 = Print expanded output
LBFGS 	              = Use the low-memory version of the BFGS optimizer
LET                   = Override certain safety checks
LEWIS 	              = Print the Lewis structure
LINMIN                = Print details of line minimization
LOCAL                 = Print localized orbitals.  These are also called Natural Bond Orbitals or NBO
LOCATE-TS 	          = Given reactants and products, locate the transition state connecting them
LOG                   = Generate a log file
MECI                  = Print details of MECI calculation
MERS=(n1,n2,n3)       = Keyword generated by MAKPOL for use with program BZ
METAL=(a[,b[,c[...]]])= Make specified atoms 100% ionic
MICROS=n              = Use specific microstates in the C.I.
MINI 	              = Reduce the size of the output by only printing specified atoms
MINMEP                = Minimize MEP minima in the plane defined
MMOK                  = Use molecular mechanics correction to CONH bonds
MNDO                  = Use the MNDO hamiltonian
MNDOD                 = Use the MNDO-d hamiltonian
MODE=n                = In EF, follow Hessian mode no. n
MOL_QMMM              = Incorporate environmental effects in the QM/MM approach
MOLDAT                = Print details of working in MOLDAT
MOLSYM                = Print details of working in MOLSYM
MOPAC                 = Use old MOPAC definition for 2nd and 3rd atoms
MOZYME 	              = Use the Localized Molecular Orbital method to speed up the SCF
MS=n                  = In MECI, magnetic component of spin
MULLIK                = Print the Mulliken population analysis
N**2                  = In excited state COSMO calculations, set the value of N**2
NLLSQ                 = Minimize gradients using NLLSQ
NOANCI                = Do not use analytical C.I. derivatives
NOCOMMENTS 	          = Ignore all lines except ATOM, HETATM, and TER in PDB files
NOGPU 	              = Do not use GPU acceleration
NOLOG                 = Suppress log file trail, where possible
NOMM                  = Do not use molecular mechanics correction to CONH bonds
NONET                 = 
NONET                 = state required
NONR                  = Do not use Newton-Raphson method in EF
NOOPT, NOOPT-X        = Do not optimize the coordinates of all atoms of type X
NOREOR                = In symmetry work, FORCE calculations, and when GEO_REF is used, use the supplied orientation
NORESEQ               = Suppress the default re-sequencing of atoms to the PDB sequence
NOSWAP 	              = Do not allow atom swapping when GEO_REF is used
NOSYM                 = Point-group symmetry set to C1
NOTER                 = Do not put "TER"s in PDB files
NOTHIEL               = Do not use Thiel's FSTMIN technique
NOTXT                 = Remove any text from atom symbols
NOXYZ                 = Do not print Cartesian coordinates
NSPA=n                = Sets number of geometric segments in COSMO
NSURF                 = Number of surfaces in an ESP calculation
OCTET                 = Octet state required
OLDCAV                = In COSMO, use the old Solvent Accessible Surface calculation
OLDENS                = Read initial density matrix off disk
OLDFPC                = Use the old fundamental physical constants
OLDGEO                = Previous geometry to be used
OMIN=n.nn             = In TS, minimum allowed overlap of eigenvectors
OPEN(n1,n2)           = Open-shell UHF or RHF calculation requested
OPT, OPT-X            = Optimize the coordinates of all atoms of type X
OPT(text=n.nn) 	      = Optimize coordinates of all atoms within n.nn Ångstroms of atoms labeled "text"
OUTPUT 	              = Reduce the amount of output (useful for large systems)
P=n.nn                = An applied pressure of n.nn Newtons/m2 to be used
PDB 	              = Input geometry is in protein data bank format
PDB=(text) 	          = User defined chemical symbols in protein data base
PDBOUT 	              = Output geometry in pdb format
PECI                  = C.I. involves paired excitations only
PI                    = Resolve density matrix into σ, π, and δ components
pKa 	              = Print the pKa for ionizable hydrogen atoms attached to oxygen atoms
PL                    = Monitor convergence of density matrix in ITER
PM3                   = Use the MNDO-PM3 Hamiltonian
PM6                   = Use the PM6 Hamiltonian
PM6-D3 	              = Use the PM6 Hamiltonian with Grimme's corrections for dispersion
PM6-DH+ 	          = Use the PM6 Hamiltonian with corrections for dispersion and hydrogen-bonding
PM6-DH2 	          = Use the PM6 Hamiltonian with corrections for dispersion and hydrogen-bonding
PM6-DH2X 	          = Use PM6 with corrections for dispersion and hydrogen and halogen bonding
PM6-D3H4 	          = Use PM6 with Řezáč and Hobza's D3H4 correction
PM6-D3H4X 	          = Use PM6 with Brahmkshatriya, et al.'s D3H4X correction
PMEP                  = Complete semiempirical MEP calculation
PM7                   = Use the PM7 Hamiltonian
PM7-TS 	              = Use the PM7-TS Hamiltonian (only for barrier heights)
PMEPR                 = Complete semiempirical MEP in a plane to be defined
POINT=n               = Number of points in reaction path
POINT1=n              = Number of points in first direction in grid calculation
POINT2=n              = Number of points in second direction in grid calculation
POLAR                 = Calculate first, second and third order polarizabilities
POTWRT                = In ESP, write out electrostatic potential to unit 21
POWSQ                 = Print details of working in POWSQ
PRECISE               = Criteria to be increased by 100 times
PRESSURE 	          = Apply pressure or tension to a solid or polymer
PRNT=n                = Print details of geometry optimization in EF
PRTCHAR               = Print charges in ARC file
PRTINT                = Print interatomic distances
PRTMEP	              = 
MEP                   = ontour data output to <filename>.mep
PRTXYZ 	              = rint Cartesian coordinates
PULAY                 = se Pulay's converger to obtain a SCF
QMMM 	              = ncorporate environmental effects in the QM/MM approach
QPMEP                 = harges derived from Wang-Ford type AM1 MEP
QUARTET	              = uartet state required
QUINTET	              = uintet state required
RABBIT 	              = enerate localized molecular orbitals with hybrid orbitals for double bonds
RAPID 	              = n MOZYME geometry optimizations, only use atoms being optimized in the SCF
RECALC=n	          = n EF, recalculate Hessian every n steps
RE-LOCAL, RE-LOCAL=n  = uring and at end of MOZYME calculation, re-localize the LMOs
RELSCF	              = efault SCF criterion multiplied by n
REORTHOG 	          = n MOZYME, re-orthogonalize LMO's each 10 SCF calculations.
RESEQ                 = e-arrange the atoms to match the PDB convention
RESIDUES 	          = abel each atom in a polypeptide with the amino acid residue
RESTART	              = alculation restarted
RHF 	              = se Restricted Hartree-Fock methods
RM1 	              = se the RM1 Hamiltonian
RMAX=n.nn	          = n TS, mximum allowed ratio for energy change
RMIN=n.nn	          = n TS, minimum allowed ratio for energy change
ROOT=n	              = oot n to be optimized in a C.I. calculation
RSCAL	              = n EF, scale p-RFO to trust radius
RSOLV=n.nn	          = ffective radius of solvent in COSMO
SADDLE	              = ptimize transition state
SCALE                 = caling factor for van der waals distance in ESP
SCFCRT=n.nn	          = efault SCF criterion replaced by the value supplied
SCINCR=n.nn           = ncrement between layers in ESP
SEPTET                = eptet state required
SETPI 	              = n MOZYME, some π bonds are explicitly set by the user
SETUP                 = xtra keywords to be read from setup file
SEXTET                = extet state required
SHIFT=n.nn            = amping factor of n defined to start SCF
SHUT <file> 	      = end a command to MOPAC to make a restart and density file, then stop.
SIGMA                 = inimize gradients using SIGMA
SINGLET               = inglet state required
SITE=(text)      	  = efine ionization state of residues in proteins
SLOG=n.nn             = n L-BFGS optimization, use fixed step of length n .nn
SLOPE                 = ultiplier used to scale MNDO charges
SMOOTH 	              = n a GRID calculation, remove artifacts caused by the order in which points are calculated
SNAP                  = ncrease precision of symmetry angles
SPARKLE 	          = se sparkles instead of atoms with basis sets
SPIN                  = rint final UHF spin matrix
START_RES(text) 	  = efine starting residue numbers in a protein, if different from the default
STATIC                = alculate Polarizability using electric fields
STEP                  = tep size in path
STEP1=n.nnn           = tep size n for first coordinate in grid calculation
STEP2=n.nnn           = tep size n for second coordinate in grid calculation
STO3G                 = eorthogonalize orbitals in STO-3G basis
SUPER                 = rint superdelocalizabilities
SYBYL                 = utput a file for use by Tripos's SYBYL program
SYMAVG                = verage symmetry equivalent ESP charges
SYMOIR                = rint characters of eigenvectors and print number of I.R.s
SYMTRZ                = rint details of working in subroutine SYMTRZ.
SYMMETRY              = mpose symmetry conditions
T=n[M,H,D]            =  time of n seconds requested
THERMO                = 
THERMO(nnn)           = 
THERMO(nnn,mmm)       = 
THERMO(nnn,mmm,lll)   = erform a thermodynamics calculation
THREADS=n 	          = et the number of threads to be used in parallelization to n
TIMES                 = rint times of various stages
T-PRIORITY            = 
T-PRIORITY=n.nn       = ime takes priority in DRC
TRANS                 = 
TRANS=n               = he system is a transition state (used in thermodynamics calculation)
TRIPLET               = riplet state required
TS                    = sing EF routine for TS search
UHF                   = se the Unrestricted Hartree-Fock method
VDW(text)             = an der waals radius for atoms in COSMO defined by user
VDWM(text) 	          = an der waals radius for atoms in MOZYME defined by user
VECTORS               = rint final vectors
VELOCITY              = upply the initial velocity vector in a DRC calculation
WILLIAMS              = se Williams surface
X-PRIORITY=n.nn       = eometry changes take priority in DRC
XENO 	              = llow non-standard residues in proteins to be labeled.
XYZ                   = o all geometric operations in Cartesian coordinates
Z=n 	              = umber of mers in a cluster
'''
