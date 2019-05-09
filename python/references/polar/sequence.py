# noinspection PyPep8Naming
class Sequence:
    """Frozen and unfrozen bit patterns for polar codes.

    The class contains frozen and unfrozen bits patterns for the specific
    message and codeword size derived from the polar sequence defined
    in TS 38.212 Rel. 15 (Version 15.2.0).

    Attributes:
        frozen_positions: Array of frozen bits positions. N - K least reliable
            positions as defined in the polar sequence.
        unfrozen_positions: Array of unfrozen bits positions. K most reliables
            positions as defined in the polar sequence.
    """

    _polar_sequence = [0, 1, 2, 7, 3, 8, 11, 24, 4, 10, 13, 28, 16, 33, 35, 76, 5, 12, 14, 32, 19, 38, 47, 80, 22, 46,
                       42, 87, 57, 95, 101, 160, 6, 17, 21, 40, 23, 45, 51, 89, 29, 55, 59, 96, 71, 108, 113, 175, 34,
                       61, 74, 111, 79, 120, 129, 186, 86, 131, 141, 208, 146, 218, 236, 327, 9, 18, 26, 54, 30, 58, 70,
                       103, 36, 75, 62, 114, 83, 123, 135, 193, 44, 73, 85, 130, 91, 138, 145, 214, 99, 148, 162, 228,
                       174, 242, 256, 357, 53, 88, 97, 144, 109, 154, 169, 239, 118, 170, 185, 250, 195, 269, 282, 382,
                       133, 191, 211, 273, 216, 283, 301, 403, 233, 307, 322, 419, 337, 434, 460, 582, 15, 25, 31, 72,
                       39, 78, 81, 134, 48, 84, 92, 143, 100, 153, 157, 238, 56, 93, 102, 155, 112, 168, 182, 252, 122,
                       183, 192, 264, 213, 279, 297, 395, 64, 106, 119, 173, 124, 184, 198, 274, 142, 209, 217, 285,
                       232, 306, 317, 418, 156, 225, 240, 311, 251, 333, 339, 432, 270, 348, 370, 453, 386, 472, 511,
                       583, 68, 121, 137, 201, 152, 215, 231, 309, 161, 234, 244, 326, 257, 338, 356, 447, 180, 253,
                       265, 346, 284, 366, 384, 478, 293, 388, 406, 494, 424, 518, 532, 641, 197, 275, 288, 373, 312,
                       394, 409, 506, 336, 415, 433, 526, 454, 535, 567, 671, 355, 440, 461, 552, 470, 577, 591, 695,
                       509, 598, 613, 690, 629, 714, 743, 830, 20, 37, 41, 90, 49, 94, 104, 167, 50, 105, 115, 176, 126,
                       194, 202, 295, 63, 116, 127, 205, 139, 212, 223, 296, 147, 222, 237, 321, 254, 335, 342, 431, 66,
                       136, 149, 207, 164, 226, 241, 334, 172, 248, 258, 344, 268, 364, 377, 468, 171, 266, 277, 363,
                       292, 385, 397, 495, 314, 411, 425, 517, 439, 531, 555, 663, 77, 159, 165, 246, 179, 262, 276,
                       358, 187, 281, 287, 383, 302, 402, 414, 515, 235, 298, 313, 405, 328, 422, 438, 528, 350, 443,
                       464, 550, 481, 576, 593, 686, 261, 324, 345, 430, 362, 452, 466, 568, 380, 475, 487, 581, 512,
                       605, 619, 707, 407, 510, 519, 614, 529, 630, 609, 721, 560, 660, 672, 749, 677, 779, 794, 846,
                       82, 177, 181, 291, 227, 305, 316, 410, 247, 320, 329, 427, 349, 445, 463, 570, 259, 347, 361,
                       446, 372, 467, 483, 585, 389, 489, 505, 601, 527, 617, 640, 725, 294, 365, 376, 482, 396, 500,
                       521, 610, 426, 522, 533, 638, 561, 627, 667, 751, 451, 546, 574, 661, 586, 676, 688, 770, 606,
                       693, 692, 790, 722, 801, 813, 877, 323, 387, 412, 523, 444, 534, 554, 647, 465, 569, 578, 673,
                       597, 679, 691, 777, 484, 589, 611, 687, 620, 694, 723, 802, 646, 729, 740, 816, 760, 834, 844,
                       905, 516, 615, 636, 724, 666, 726, 756, 821, 670, 753, 772, 840, 786, 853, 870, 924, 680, 780,
                       798, 859, 808, 873, 865, 930, 828, 885, 893, 946, 909, 954, 963, 984, 27, 43, 52, 98, 60, 117,
                       128, 199, 65, 132, 140, 204, 151, 220, 224, 330, 67, 150, 158, 219, 166, 263, 271, 354, 188, 272,
                       290, 381, 304, 398, 413, 525, 69, 163, 178, 267, 190, 289, 299, 392, 200, 308, 318, 416, 332,
                       435, 449, 536, 210, 325, 341, 442, 359, 462, 473, 564, 367, 469, 490, 588, 493, 600, 616, 745,
                       107, 189, 196, 303, 206, 319, 331, 429, 229, 343, 351, 457, 369, 477, 488, 572, 245, 353, 375,
                       471, 391, 492, 497, 594, 404, 498, 504, 618, 545, 631, 656, 752, 260, 390, 400, 503, 421, 520,
                       524, 624, 437, 544, 557, 645, 580, 664, 674, 773, 456, 566, 587, 675, 607, 685, 709, 787, 635,
                       712, 730, 803, 741, 819, 836, 903, 110, 203, 221, 340, 243, 352, 371, 480, 255, 378, 393, 499,
                       408, 508, 513, 621, 280, 401, 420, 514, 436, 541, 553, 642, 455, 562, 579, 669, 595, 681, 700,
                       774, 300, 428, 448, 556, 474, 575, 573, 682, 485, 590, 599, 696, 625, 710, 718, 805, 507, 608,
                       633, 715, 643, 735, 742, 822, 659, 750, 764, 841, 789, 855, 871, 925, 315, 459, 476, 592, 496,
                       604, 626, 713, 539, 634, 650, 738, 653, 744, 758, 833, 547, 651, 658, 755, 683, 763, 783, 852,
                       704, 788, 797, 860, 812, 878, 888, 933, 563, 689, 698, 775, 719, 791, 800, 867, 731, 810, 823,
                       884, 837, 894, 907, 949, 766, 825, 842, 897, 857, 911, 916, 961, 868, 921, 929, 966, 940, 974,
                       983, 1003, 125, 230, 249, 379, 278, 399, 417, 530, 286, 423, 441, 543, 458, 559, 584, 701, 310,
                       450, 479, 571, 491, 603, 596, 706, 501, 612, 628, 728, 648, 736, 747, 829, 360, 486, 502, 602,
                       538, 623, 637, 739, 542, 649, 655, 748, 665, 759, 769, 848, 548, 662, 678, 768, 703, 782, 795,
                       861, 716, 807, 811, 879, 824, 889, 900, 944, 368, 537, 540, 644, 549, 652, 668, 762, 565, 684,
                       697, 778, 711, 792, 809, 875, 632, 702, 720, 796, 732, 817, 826, 886, 761, 827, 843, 898, 858,
                       910, 915, 960, 654, 734, 754, 818, 767, 839, 850, 902, 785, 854, 863, 914, 874, 922, 932, 969,
                       799, 869, 881, 928, 892, 935, 943, 976, 904, 947, 953, 981, 958, 989, 991, 1011, 374, 551, 558,
                       699, 622, 708, 717, 806, 639, 727, 737, 820, 757, 832, 847, 901, 657, 746, 765, 835, 776, 851,
                       864, 913, 793, 872, 862, 919, 887, 931, 939, 972, 705, 771, 781, 856, 804, 866, 880, 926, 815,
                       882, 891, 936, 899, 941, 950, 980, 838, 895, 906, 945, 917, 955, 959, 987, 923, 965, 968, 993,
                       975, 996, 998, 1008, 733, 784, 814, 883, 831, 890, 896, 942, 845, 908, 912, 952, 920, 956, 967,
                       990, 849, 918, 927, 964, 938, 970, 971, 997, 948, 977, 979, 999, 985, 1004, 1006, 1016, 876, 934,
                       937, 973, 951, 978, 982, 1001, 957, 986, 988, 1005, 994, 1007, 1012, 1018, 962, 992, 995, 1009,
                       1000, 1010, 1013, 1019, 1002, 1014, 1015, 1020, 1017, 1021, 1022, 1023]
    """Reliability of first 1024 bits as defined in TS 38.212 Rel. 15 (Version 15.2.0).

    The element n-th in the array represents the reliability of the n-th bits position
    as defined in the standard. The higher the reliability is the more reliable the
    bit positions is.

    Example:
        The bit position 3 is the 7th least reliable bit position in the full sequence.
    """

    def __init__(self, N, K):
        """Construct frozen and unfrozen bits patterns.

        The constructor generates frozen and unfrozen bit sequences for a given codeword
        and message size.

        Args:
            N: Codeword size. It must be in range [1, 1024].
            K: Message size. It must be in range [1, 1024] and K <= N.

        Raises:
            ValueError: At least one of the arguments is invalid.
        """
        if N > 1024:
            raise ValueError('Codeword size has to be less than 1024 (Order = 10)!')
        if K > N:
            raise ValueError('Message size cannot exceed codeword size!')

        reliabilities = Sequence._polar_sequence[:N]
        positions = range(N)
        positions_with_reliabilities = [(q, wq) for q, wq in zip(positions, reliabilities)]
        sorted_bits_positions = sorted(positions_with_reliabilities, key=lambda x: x[1])
        sorted_positions = [q for (q, _) in sorted_bits_positions]
        self.frozen_positions = sorted_positions[:N - K]
        self.unfrozen_positions = sorted_positions[N - K:]
