# from __future__ import absolute_import
#
# import errno
# import os
# import subprocess
# import sys
# from collections import namedtuple
#
# virtual_devices = ["Nougat_7.1.1", "Oreo_8.1", "Pie_9.0", "Android_10.0"]
# APP_PATH = 'apps/ShazzleChat-0.5.3(75)-debug.apk'
# APK_VERSION = APP_PATH.split("-")[1]
# Test_Suit = namedtuple('Test_Suit', ['test_path', 'n_device'])
#
#
# def full_coverage_testing():
#     # installation_test = Test_Suit("test_suites/test_suit_installation.py", 1)
#     # registration_test = Test_Suit("test_suites/test_suit_registration.py", 1)
#     # contacts_test = Test_Suit("test_suites/test_suit_contacts.py", 2)
#     # direct_chatting_test = Test_Suit("test_suites/test_suit_direct_chatting.py", 3)
#     # group_chatting_test = Test_Suit("test_suites/test_suit_group_chatting.py", 3)
#     # saved_messages_test = Test_Suit("test_suites/test_suit_saved_messages.py", 2)
#
#     # test_suites = [installation_test, registration_test, contacts_test,
#     #                direct_chatting_test, group_chatting_test, saved_messages_test]
#
#     # create_testing_process_and_log_file(test_suites)
#     pass
#
#
# def create_testing_process_and_log_file(test_suites):
#     for device_i in range(0, len(virtual_devices)):
#
#         filename = "logs/" + APK_VERSION + "/" + sys.argv[1] + "testing_of_{virtual_dev}.log" \
#             .format(virtual_dev=virtual_devices[device_i])
#         if not os.path.exists(os.path.dirname(filename)):
#             try:
#                 os.makedirs(os.path.dirname(filename))
#             except OSError as exc:  # Guard against race condition
#                 if exc.errno != errno.EEXIST:
#                     raise
#
#         log_results = []
#
#         for test_suit in test_suites:
#
#             args = [test_suit.test_path, "-v", "--app_path", APP_PATH]
#             emulators_copy = virtual_devices.copy()
#             emulators_copy[0], emulators_copy[device_i] = emulators_copy[device_i], emulators_copy[0]
#
#             for emulator_i in range(0, test_suit.n_device):
#                 args.append("--emulator_" + str(emulator_i + 1))
#                 args.append(emulators_copy[emulator_i])
#
#             p = subprocess.Popen(['pytest'] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#             output, err = p.communicate()
#             log_results.append(output.decode("utf-8"))
#
#             print(output.decode("utf-8"))
#             print(err.decode("utf-8"))
#             p.wait()
#             p.kill()
#
#         logFile = open(filename, 'w')
#         logFile.write("\n".join(log_results))
#         logFile.close()
#
#
# #
# if __name__ == '__main__':
#     if sys.argv[1] == 'full_coverage':
#         full_coverage_testing()
