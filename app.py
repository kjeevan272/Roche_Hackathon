from flask import Flask, jsonify, request
from collections import Counter

app = Flask(__name__)
stats = Counter()

@app.route('/fizzbuzz')
def fizz_buzz():
    int1 = int(request.args.get('int1', 3))
    str1 = request.args.get('str1', 'fizz')
    int2 = int(request.args.get('int2', 5))
    str2 = request.args.get('str2', 'buzz')
    limit = int(request.args.get('limit', 100))

    result = []
    for i in range(1, limit + 1):
        if i % int1 == 0 and i % int2 == 0:
            result.append(str1 + str2)
        elif i % int1 == 0:
            result.append(str1)
        elif i % int2 == 0:
            result.append(str2)
        else:
            result.append(str(i))

    stats[(int1, int2, str1, str2, limit)] += 1

    return jsonify(result)

@app.route('/stats')
def statistics():
    most_common = stats.most_common(1)
    if most_common:
        ((int1, int2, str1, str2, limit), count) = most_common[0]
        return jsonify({'int1': int1, 'int2': int2, 'str1': str1, 'str2': str2, 'limit': limit, 'count': count})
    else:
        return jsonify({})

if __name__ == '__main__':
    app.run(debug=True)
