from dataclasses import dataclass
from typing import Tuple

from src import robots

import numpy as np


# TODO: Store data in `KnownKinematicMapping` objects.  
# @dataclass
# class KnownKinematicMapping:

#     configs: np.ndarray
#     poses: np.ndarray

#     def __post_init__(self):
#         assert self.configs.shape[0] == self.poses.shape[0]
#         assert self.poses.shape[1] == 7

# atlas_data = KnownKinematicMapping(configs=[], poses=[])


def get_gt_samples_and_endpoints(robot: robots.KlamptRobotModel) -> Tuple[np.array, np.array]:
    """ Data store for joint space - cartesian space maps. There are better ways to store this, I know. 

    Args:
        robot (robots.KlamptRobotModel): _description_

    Raises:
        ValueError: _description_

    Returns:
        Tuple[np.array, np.array]: _description_
    """

    if isinstance(robot, robots.Atlas):
        samples = np.array(
            [
                [
                    -0.16071900365413277,
                    -0.5647552036190518,
                    -0.41432069939065946,
                    1.1108391114920957,
                    0.16997202387819232,
                    2.3574419303793404,
                    1.4072475837547618,
                    1.07054427730212,
                    0.5388592450910359,
                ],
                [
                    -0.1335797496428427,
                    -0.7443145444062369,
                    -0.655880467182391,
                    1.8656140922410411,
                    0.7902679346046189,
                    1.0246341287936904,
                    0.8984381173692961,
                    0.3971786434636564,
                    0.29946276553309353,
                ],
                [
                    0.1466147110768612,
                    -0.9678629505566342,
                    0.6271332639182156,
                    -0.6911456969664758,
                    1.4888147071850428,
                    1.5759030634109614,
                    0.7635815058031575,
                    -1.167097128284174,
                    0.2124959954824867,
                ],
                # Next three are from trac-ik
                (
                    0.6098422199843345,
                    0.39591305792074133,
                    -0.7837180051370695,
                    1.6223150156697204,
                    1.559423753377537,
                    0.7115447674645303,
                    1.5510962654270868,
                    0.4863195573080535,
                    0.45320749800482524,
                ),
                (
                    0.20295307816646357,
                    -1.0714002726125396,
                    -0.5885052608552014,
                    -0.24988900069189596,
                    0.20849768465379484,
                    2.2622520162719506,
                    0.0,
                    1.4513733938809834,
                    0.6431599111316134,
                ),
                (
                    0.3202159669444278,
                    -0.644705226964653,
                    0.785176280565938,
                    1.4956636882254297,
                    0.05748706714493193,
                    0.014121718062555194,
                    1.0658532080517331,
                    -1.5670741991444586,
                    0.7054582408653545,
                ),
            ]
        )
        endpoints = np.array(
            [
                [
                    -0.16606006913201427,
                    0.6910107021998343,
                    -0.03565974503316812,
                    -0.09248629598384732,
                    0.24939559078104767,
                    0.5560707746217297,
                    -0.7874220075447154,
                ],
                [
                    -0.10527239417941561,
                    0.9334080152215245,
                    0.19314742009400387,
                    0.29520960413935765,
                    0.19779641588782862,
                    0.8740856424942338,
                    -0.3312131595683594,
                ],
                [
                    -0.6756261323667903,
                    -0.37969239336195193,
                    0.6454608614726247,
                    0.23910770032117873,
                    0.9233786429710236,
                    0.04607763404172943,
                    0.29677641583054526,
                ],
                [
                    -0.16606006913201427,
                    0.6910107021998343,
                    -0.03565974503316812,
                    -0.09248629598384732,
                    0.24939559078104767,
                    0.5560707746217297,
                    -0.7874220075447154,
                ],
                [
                    -0.10527239417941561,
                    0.9334080152215245,
                    0.19314742009400387,
                    0.29520960413935765,
                    0.19779641588782862,
                    0.8740856424942338,
                    -0.3312131595683594,
                ],
                [
                    -0.6756261323667903,
                    -0.37969239336195193,
                    0.6454608614726247,
                    0.23910770032117873,
                    0.9233786429710236,
                    0.04607763404172943,
                    0.29677641583054526,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.Baxter):
        samples = np.array(
            [
                [
                    -0.9127556307920636,
                    0.32674131091735603,
                    -1.0299190296861118,
                    1.625623056177867,
                    -3.034484776045919,
                    1.3565924414485488,
                    -0.13131239598348987,
                ],
                [
                    1.643315289424271,
                    -0.7616038400905532,
                    -0.20135846232163335,
                    2.4679407934267585,
                    2.1210875876291153,
                    -0.7495489710612356,
                    0.00432746813529894,
                ],
                [
                    -0.06622471718764111,
                    -1.6573709171419844,
                    2.6693229938384286,
                    1.021287178581988,
                    -3.008567473667986,
                    -0.35840834234897345,
                    1.5359995468853311,
                ],
                [
                    1.4800248913293683,
                    -0.9420956101010582,
                    -0.48371643968601274,
                    0.19749972807390748,
                    -2.947181869822705,
                    1.200965970488356,
                    1.764629878709874,
                ],
                [
                    -0.6091386605091589,
                    -1.9348662803797452,
                    1.5080198346605513,
                    1.5057699317196416,
                    1.596137532029517,
                    1.3708111179595015,
                    -2.9243482666354033,
                ],
            ]
        )
        endpoints = np.array(
            [
                [
                    0.5391789643275974,
                    -0.25058202750502256,
                    -0.009739012453285262,
                    0.4254526572175882,
                    0.7535633003343233,
                    0.32905744650009316,
                    0.3779597673808346,
                ],
                [
                    0.031197584640113712,
                    0.5408787751738287,
                    0.09767518272035537,
                    0.45192475530882886,
                    -0.0741500599110992,
                    0.8886729826959593,
                    0.0229371746408042,
                ],
                [
                    -0.5096336362389801,
                    0.1132732909644481,
                    0.9630529585991809,
                    0.42951534567255567,
                    -0.4068421826254288,
                    -0.5264992242489868,
                    0.6105690568097744,
                ],
                [
                    -0.256748756191486,
                    0.6626321121590478,
                    1.1336336623857752,
                    0.9254705990663897,
                    0.20606533569732965,
                    -0.043986746215529636,
                    0.314811711734197,
                ],
                [
                    -0.2828712459360646,
                    0.706518507469001,
                    0.6989806673063261,
                    0.42323142689637777,
                    -0.6158184623497436,
                    -0.5244558449303947,
                    0.4081529706308646,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.AtlasArm):
        samples = np.array(
            [
                [
                    0.5904442944262882,
                    1.6834647877915845,
                    1.7924622753538533,
                    1.3532900551770215,
                    1.3359449803779164,
                    0.06248178860115122,
                ],
                [
                    1.4475807346357448,
                    1.1255759804181704,
                    1.933924102417314,
                    0.9698621062082533,
                    1.0771805426346452,
                    -0.10839555606921442,
                ],
                [
                    1.6307351030638741,
                    1.6549210144943254,
                    2.1766755398146462,
                    0.4175332603296874,
                    -0.9207620210321553,
                    -0.0667461309277812,
                ],
            ]
        )
        endpoints = np.array(
            [
                [
                    0.28661160072728037,
                    0.4456910813740922,
                    0.7616369665483941,
                    -0.6548334003490328,
                    0.285458026570377,
                    0.6445203088934088,
                    0.27258118841514795,
                ],
                [
                    -0.04900693488879822,
                    0.6620592520777435,
                    0.7850660300724548,
                    -0.5948444120897644,
                    -0.0618169747940414,
                    0.8003094432087163,
                    0.04293695545622627,
                ],
                [
                    0.2181761337882501,
                    0.5744884898687439,
                    0.8503228469515163,
                    -0.004997856687190606,
                    0.16355938627061697,
                    0.9233544777120418,
                    0.34733248779870274,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.PandaArm):
        samples = np.array(
            [
                [
                    -1.5110527997865721,
                    0.11748990374779456,
                    2.4246351088245013,
                    -1.0974982437047172,
                    0.8580315157310916,
                    2.690195426145167,
                    -0.15217243963383043,
                ],
                [
                    -2.5195540652085575,
                    -1.0923886316503646,
                    -0.25334633207036994,
                    -2.50685953160908,
                    -1.8514660249557031,
                    1.281564167326434,
                    2.2991345538186327,
                ],
                [
                    -0.7318684054626723,
                    0.653763200586835,
                    2.485134580170451,
                    -1.9374205554575694,
                    0.15447884855232674,
                    3.7940906679030593,
                    -1.055677486533202,
                ],
            ]
        )
        endpoints = np.array(
            [
                [
                    0.3276691444989038,
                    0.30042266416705926,
                    1.015338771196833,
                    -0.41606621289863777,
                    0.46674406793332446,
                    0.38821981752600343,
                    0.6769964954217373,
                ],
                [
                    -0.25575071784967085,
                    0.09752348216036198,
                    0.6966252367115788,
                    0.5658888072465215,
                    -0.47534101373150484,
                    -0.5178967752177974,
                    -0.43081748887065957,
                ],
                [
                    0.15233876418467032,
                    0.3346856828425311,
                    0.8817122583215848,
                    -0.11649377346206646,
                    0.13526289388514603,
                    0.39913759404492616,
                    0.8993455016301645,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.Robonaut2):
        samples = np.array(
            [
                [
                    1.4458748580971288,
                    -2.4327509053508285,
                    -0.5520648762465206,
                    -4.04472355775279,
                    -0.28417159662429015,
                    3.6846479622398642,
                    0.4905273850735543,
                    -0.565012603294634,
                ],
                [
                    0.0854495972391014,
                    -0.9688181886477896,
                    -1.542001002253481,
                    -4.500137166909969,
                    -0.7847420743748206,
                    2.804364219216722,
                    -0.4861213913312062,
                    -0.45488649619441623,
                ],
                [
                    -1.4194034547587648,
                    1.8302724138713922,
                    -0.7257386580698967,
                    -3.892901100278454,
                    -1.1957633638441127,
                    1.7186530248049783,
                    0.22668312835611504,
                    -0.026668791554108395,
                ],
            ]
        )
        endpoints = np.array(
            [
                [
                    0.9002736014456193,
                    -0.3467538792259893,
                    0.7317990463155233,
                    -0.8350494338902836,
                    -0.20360892492902294,
                    -0.14600329742678614,
                    0.48981515471580783,
                ],
                [
                    0.4421501636511391,
                    0.23507374858780894,
                    -0.03969231397014562,
                    -0.8850091285256003,
                    0.021047144267192508,
                    -0.38313207793340975,
                    0.2636772098664977,
                ],
                [
                    -0.8549992036365924,
                    0.230216169239771,
                    0.8295534745844333,
                    0.33413232092069833,
                    -0.3728077311104978,
                    -0.8562563442012763,
                    -0.12725981594932528,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.Robonaut2Arm):
        samples = np.array(
            [
                [
                    -2.130022030725849,
                    -0.44682983155414013,
                    -3.4907904444152433,
                    -1.3397211987232411,
                    0.8189395642898818,
                    -0.5384328793911296,
                    -0.527547279335315,
                ],
                [
                    0.8042901589628157,
                    -1.4986234717512745,
                    -1.5649149878112056,
                    -2.6616606198215345,
                    -0.7398228401966358,
                    0.444900379868016,
                    0.014294719504506337,
                ],
                [
                    2.7833008930043848,
                    -0.4569815286352368,
                    -3.7582439640261303,
                    -1.6014761598897667,
                    -1.321167429587978,
                    -0.13788548078396956,
                    -0.271862858115824,
                ],
            ]
        )
        endpoints = np.array(
            [
                [
                    0.1502987000451928,
                    0.8852401938609314,
                    0.3664859266926507,
                    -0.38283564922465907,
                    0.18512714300760202,
                    0.4394599307631098,
                    -0.7912267537553697,
                ],
                [
                    0.16752115266460857,
                    0.2600237585320411,
                    0.309827534823251,
                    -0.9023800930409365,
                    0.31303006977434633,
                    -0.08223646653472486,
                    0.2845338409967825,
                ],
                [
                    0.4227345616202602,
                    0.7151303437282903,
                    0.5069465290909269,
                    -0.9063574420376184,
                    -0.2898759102343578,
                    -0.2125962017621246,
                    0.2220157627853171,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.Valkyrie):
        samples = np.array(
            [
                [
                    0.9993996795611186,
                    0.002438609574043016,
                    0.13873351994828334,
                    -0.6794944422779894,
                    0.7233282649736867,
                    -0.13297320978876437,
                    -0.8707855212782658,
                    0.7502328457742826,
                    -0.46889556885106976,
                    -0.3071979672569819,
                ],
                [
                    -0.07888372984949643,
                    0.03341591158691298,
                    0.2527232073870296,
                    1.0737347490878952,
                    -0.22822313516212556,
                    1.2082769810162284,
                    -0.540209729650108,
                    3.0452392396591037,
                    -0.14893815333646082,
                    -0.33742121210630327,
                ],
                [
                    -0.11302006233556638,
                    0.3911584167976776,
                    0.16601167578502554,
                    -1.7460358772174671,
                    0.5123494675155815,
                    -0.588301621897183,
                    -1.186542579502575,
                    0.8501922764269931,
                    -0.08321596280635235,
                    -0.05446735081477755,
                ],
            ]
        )
        endpoints = np.array(
            [
                [
                    -0.46576165274342296,
                    0.24247920993566044,
                    0.8342639576619026,
                    0.8704834285589543,
                    0.2220558624089733,
                    0.3505758567071594,
                    0.2646627349441095,
                ],
                [
                    -0.13241502884871653,
                    0.7490103863433752,
                    0.34437962569530467,
                    -0.8685944581371092,
                    -0.009224826908970377,
                    0.4881435860488527,
                    -0.08470188463882017,
                ],
                [
                    -0.07967204493898322,
                    0.502363838957376,
                    0.6954537200051969,
                    0.6541775241462621,
                    0.6829918033659986,
                    -0.32074306617321785,
                    -0.05194082150419371,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.ValkyrieArm):
        samples = np.array(
            [
                [-0.927690417061511, 2.4119191831687443, 0.3003743705753924, 0.2996766044522322],
                [-1.0748543295292423, 0.1307298076682888, -0.5296275898079573, -0.31640885354196396],
                [0.10439095701002143, 1.3111442041092616, -0.47624179698571517, 0.10503890651694603],
            ]
        )
        endpoints = np.array(
            [
                [
                    0.25022609068710855,
                    0.7723952384770082,
                    0.3187,
                    0.29235796251078194,
                    0.575567355301436,
                    0.7243832582927328,
                    -0.24190480849511536,
                ],
                [
                    0.2761335800801039,
                    0.7388593411582531,
                    0.3187,
                    0.7502637714536716,
                    -0.2192772960498532,
                    0.15524750951219365,
                    -0.6040860464134554,
                ],
                [
                    -0.019467967111583273,
                    0.86279037089557,
                    0.3187,
                    0.7510822369715284,
                    -0.18678756836527513,
                    0.5924719033075413,
                    0.22352387210580366,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.ValkyrieArmShoulder):
        samples = np.array(
            [
                [
                    -1.004836028006292,
                    0.6585400038213758,
                    0.03505970337274178,
                    -0.8813298640960916,
                    -1.0516097534093052,
                    0.37327300609540515,
                    0.019132653981638215,
                ],
                [
                    0.8217431845874055,
                    0.32889535012537396,
                    -2.5840095619956003,
                    -0.5576340670070381,
                    2.4454170226247047,
                    -0.17650555288520436,
                    0.22157617590482703,
                ],
                [
                    0.5997718319389325,
                    0.7490893685809559,
                    -1.597823769411329,
                    -1.65655511693725,
                    1.1654578334288037,
                    -0.12674420590676577,
                    0.3704225758259342,
                ],
            ]
        )
        endpoints = np.array(
            [
                [
                    -0.13554312189950363,
                    0.6757835834651359,
                    0.6845839272501097,
                    0.5154980411724746,
                    0.370769986660443,
                    -0.7233052744370394,
                    -0.27133165408907883,
                ],
                [
                    0.11629176600904827,
                    0.7788587043801494,
                    0.5977379979954276,
                    0.8979813022884305,
                    0.32176363608001934,
                    0.23271726023511136,
                    0.18957958757630614,
                ],
                [
                    0.26002278837848625,
                    0.2785971750475017,
                    0.6988980274357134,
                    0.48476264670205016,
                    0.7918349670783773,
                    -0.09656210175413493,
                    -0.35871760728912183,
                ],
            ]
        )
        return samples, endpoints

    if isinstance(robot, robots.Pr2):
        samples = np.array(
            [
                [
                    0.22892427434763876,
                    -0.5772635451280383,
                    0.3556751264022998,
                    2.286899822960674,
                    -1.274642031477776,
                    -2.8308331886877807,
                    -0.43722313367664345,
                    1.5863768291812796,
                ],
                [
                    0.2301940319720962,
                    0.3345681448072457,
                    -0.29767369604638094,
                    -0.28157275198387044,
                    -2.101971870282185,
                    0.12301754178010871,
                    -1.5172336830366024,
                    -1.3785310629351433,
                ],
                [
                    0.28052755686385455,
                    1.8148591519678812,
                    0.24819826950254142,
                    -0.15154258848022784,
                    -0.6415633052907614,
                    -0.0976336846284056,
                    -1.8692543939209827,
                    0.3758889633631961,
                ],
                [
                    0.09185042714929406,
                    1.174033912304452,
                    -0.46410506332416906,
                    1.1907524408595134,
                    -1.4033437201459504,
                    -1.6002018054653857,
                    -0.07288182231624418,
                    -1.3603233931990428,
                ],
                [
                    0.31125557342811266,
                    0.38342776464484896,
                    0.7726781194316917,
                    0.010080153852257911,
                    -1.9590533155748797,
                    -2.606936876573345,
                    -1.415188098929268,
                    -1.14026196311222,
                ],
            ]
        )
        endpoints = np.array(
            [
                [
                    0.2363809701032868,
                    -0.274908225070011,
                    0.6587552052010912,
                    0.618303452055348,
                    0.3717288152215499,
                    0.06728014734190642,
                    -0.689196569118038,
                ],
                [
                    0.1599207430645216,
                    0.34239599247619873,
                    1.3446754194287738,
                    0.1598705084927284,
                    -0.41528095765372736,
                    0.7516823572109156,
                    0.48678206682489983,
                ],
                [
                    -0.267516105403933,
                    0.9414522846336906,
                    1.0938441310774087,
                    0.04493652164605103,
                    0.6984617050715256,
                    -0.508954258288508,
                    0.501096316630771,
                ],
                [
                    0.39613828184941535,
                    0.49220276192214085,
                    1.1905162677084262,
                    0.8207335749128942,
                    -0.47606179881532074,
                    -0.10955558707092916,
                    -0.2962416852182789,
                ],
                [
                    0.4211104893756856,
                    0.37481323825715085,
                    1.120269641373399,
                    0.43821584068427494,
                    0.7801726057761867,
                    0.4270868048352854,
                    0.12997862634047247,
                ],
            ]
        )
        return samples, endpoints

    raise ValueError(f"robot '{robot.name}' not recognized")


if __name__ == "__main__":
    robot = robots.Atlas()
    get_gt_samples_and_endpoints(robot)
