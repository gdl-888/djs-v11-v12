# -*- coding: utf-8 -*-

import re
import sys

if sys.version_info > (3, 0):
    raw_input = input;
    
txtFileName = '';
txtDestPath = '';

def efp(x = '', sep = '', end = ''):
    return;
def efi(x = ''):
    return;

if(len(sys.argv) >= 2):
    txtFileName = sys.argv[1];
    txtDestPath = sys.argv[2];
    
    print = efp;
    input = efi;
    
    try:
        raw_input = efi;
    except:
        pass;
else:
    txtFileName = raw_input("원본 코드 경로/이름: ");
    txtDestPath = raw_input("대상 화일 경로/이름: ");

txtCode = open(txtFileName, "r", encoding="utf-8").read();

txtCode = re.sub("[.]get", ".cache.get", txtCode); print("cache로 업데이트 중...");
txtCode = re.sub("[.]find", ".cache.find", txtCode);

txtCode = re.sub("[.]fetchUser", ".users.fetch", txtCode); print("fetch 업데이트 중...");
txtCode = re.sub("[.]fetchMessage", ".messages.fetch", txtCode);
txtCode = re.sub("[.]fetchMember", ".members.fetch", txtCode);
txtCode = re.sub("[.]fetchPinnedMessages", ".messages.fetchPinned", txtCode);

txtCode = re.sub("[.]addRole", ".roles.add", txtCode); print("addRole => roles.add로...");
txtCode = re.sub("[.]removeRole", ".roles.remove", txtCode); print("removeRole => roles.remove로...");
txtCode = re.sub("[.]setRoles", ".roles.set", txtCode); print("기타 역할 명령 업데이트 중...");

txtCode = re.sub("[.]colorRole", ".roles.color", txtCode);
txtCode = re.sub("[.]highestRole", ".roles.highest", txtCode);
txtCode = re.sub("[.]hoistRole", ".roles.hoist", txtCode);

txtCode = re.sub("[.]avatarURL", ".avatarURL()", txtCode); print("URL 변수 업데이트 중...");
txtCode = re.sub("[.]displayAvatarURL", ".displayAvatarURL()", txtCode);
txtCode = re.sub("[.]iconURL", ".iconURL()", txtCode);
txtCode = re.sub("[.]splashURL", ".splashURL()", txtCode);

txtCode = re.sub("[.]ban", ".members.ban", txtCode); print("ban => members.ban로...");
txtCode = re.sub("[.]unban", "members.unban", txtCode); print("unban => members.unban로...");

txtCode = re.sub("[.]sendMessage", ".send", txtCode); print("메시지 함수 업데이트 중...");
txtCode = re.sub("[.]sendEmbed", ".send", txtCode);
txtCode = re.sub("[.]RichEmbed", ".MessageEmbed", txtCode);

print("exists(a, b) => find(x => x.a == b)로...");
txtCode = re.sub('[.]users[.]exists\s{0,}[(]\s{0,}(\'|\"|`)(?P<ik>(?:(?!(\'|\"|`)).)+)(\'|\"|`)\s{0,}[,]\s{0,}(\'|\"|`)(?P<iv>(?:(?!(\'|\"|`)).)+)(\'|\"|`)\s{0,}[)]', ".users.cache.some(user => user.\g<ik> == `\g<iv>`)", txtCode);
print("find(a, b) => find(x => x.a == b)로...");
txtCode = re.sub('[.]users[.]cache[.]find\s{0,}[(]\s{0,}(\'|\"|`)(?P<ik>(?:(?!(\'|\"|`)).)+)(\'|\"|`)\s{0,}[,]\s{0,}(\'|\"|`)(?P<iv>(?:(?!(\'|\"|`)).)+)(\'|\"|`)\s{0,}[)]', ".users.cache.find(user => user.\g<ik> == `\g<iv>`)", txtCode);

txtCode = re.sub("[.]findAll", ".filterArray", txtCode);

print("음성 함수 업데이트 중...");
txtCode = re.sub("[.]playFile", ".play", txtCode);
txtCode = re.sub("[.]playStream\s{0,}[(](?P<is>(?:(?![)]).)+)[)][.]setBitrate\s{0,}[(]\s{0,}(?P<ib>(?:(?![)]).)+)\s{0,}[)]", ".play(\g<is>, { bitrate: \g<ib> })", txtCode);
txtCode = re.sub("[.]playStream", ".play", txtCode);
txtCode = re.sub("[.]playArbitraryInput", ".play", txtCode);
txtCode = re.sub("[.]playBroadcast", ".play", txtCode);
txtCode = re.sub('[.]playOpusStream\s{0,}[(](?P<is>(?:(?![)]).)+)\s{0,}[)]', '.play(\g<is>, { type: "opus" })', txtCode);
txtCode = re.sub('[.]playConvertedStream\s{0,}[(](?P<is>(?:(?![)]).)+)\s{0,}[)]', '.play(\g<is>, { type: "converted" })', txtCode);

print("기타 함수 업데이트 중...");
txtCode = re.sub('[.]end\s{0,}[(]\s{0,}[)]', '.destroy()', txtCode);
txtCode = re.sub('[.]on\s{0,}[(](\'|"|`)end(\'|"|`)\s{0,}[,]', '.on("finish",', txtCode);

txtCode = re.sub('[.]createVoiceBroadcast', '.createVoiceBroadcast', txtCode);
txtCode = re.sub('[.]dispatchers', '.subscribers', txtCode);

txtCode = re.sub('[.]broadcasts', '.voice.broadcasts', txtCode);

txtCode = re.sub('[.]on\s{0,}[(]\s{0,}(\'|"|`)disconnect(\'|"|`)\s{0,}[,]\s{0,}function\s{0,}[(]\s{0,}(?P<ie>(?:(?![)]).)+)\s{0,}[)]', ".on('shardDisconnect', function(\g<ie>, shardID)", txtCode);
txtCode = re.sub('[.]on\s{0,}[(]\s{0,}(\'|"|`)disconnect(\'|"|`)\s{0,}[,]\s{0,}([(]|)\s{0,}(?P<ie>(?:(?![)]).)+)\s{0,}([)]|)\s{0,}[=][>]', ".on('shardDisconnect', (\g<ie>, shardID) =>", txtCode);

txtCode = re.sub('[.]on\s{0,}[(]\s{0,}(\'|"|`)reconnecting(\'|"|`)\s{0,}[,]\s{0,}function\s{0,}[(]\s{0,}[)]', ".on('shardReconnecting', function(id)", txtCode);
txtCode = re.sub('[.]on\s{0,}[(]\s{0,}(\'|"|`)reconnecting(\'|"|`)\s{0,}[,]\s{0,}[(]\s{0,}[)]\s{0,}[=][>]', ".on('shardReconnecting', id =>", txtCode);

txtCode = re.sub('[.]on\s{0,}[(]\s{0,}(\'|"|`)resume(\'|"|`)\s{0,}[,]\s{0,}function\s{0,}[(]\s{0,}(?P<ie>(?:(?![)]).)+)\s{0,}[)]', ".on('shardResume', function(\g<ie>, shardID)", txtCode);
txtCode = re.sub('[.]on\s{0,}[(]\s{0,}(\'|"|`)resume(\'|"|`)\s{0,}[,]\s{0,}([(]|)\s{0,}(?P<ie>(?:(?![)]).)+)\s{0,}([)]|)\s{0,}[=][>]', ".on('shardResume', (\g<ie>, shardID) =>", txtCode);

txtCode = re.sub('[.]ping', '.ws.ping', txtCode);
txtCode = re.sub('[.]status', '.ws.status', txtCode);

txtCode = re.sub('[.]voiceConnections', '.voice.connections', txtCode);

print("setGame => setActivity로...");
txtCode = re.sub('[.]setGame\s{0,}[(]\s{0,}(\'|"|`)(?P<is>(?:(?!(\'|"|`)).)+)(\'|"|`)\s{0,}[)]', '.setActivity(`\g<is>`)', txtCode);
txtCode = re.sub('[.]setGame\s{0,}[(]\s{0,}(\'|"|`)(?P<is>(?:(?!(\'|"|`)).)+)(\'|"|`)\s{0,}[,]\s{0,}(\'|"|`)(?P<it>(?:(?!(\'|"|`)).)+)(\'|"|`)\s{0,}[)]', '.setActivity(`\g<is>`, { url: "\g<it>", type: "STREAMING" })', txtCode);

x = raw_input("\r\n변환이 완료되었으며 저장하기 전에 경고: 대상 화일이 있으면 오류가 발생할 수 있읍니다. 계속하려면 리턴글쇠를 누르십시오. . . ");
f = open(txtDestPath, "w+", encoding='utf-8');
f.write(txtCode);
f.close();

print("\r\n처리되었읍니다.");
